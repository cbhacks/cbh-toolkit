set -e

sudo apt-get update -qq
sudo apt-get install -qq p7zip-full

PKG_DIR="$(mktemp -d)"

pkg() {
    cp -r "$1" "${PKG_DIR}/$(basename "$1")"
}

pkg 'stage2-script.py'
pkg 'content'

RESULT_FILE=$( \
    printf \
    'cbh-toolkit-stage2-%04d-%s.zip' \
    "${TRAVIS_BUILD_NUMBER}" \
    "${TRAVIS_COMMIT}" \
)

rm -f "${RESULT_FILE}"
7z a "${RESULT_FILE}" "${PKG_DIR}/"'*'

(
    # Don't deploy for pull requests (it will fail, no S3 keys).
    if [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
        echo 'No artifacts will be deployed; this is a pull request'
        exit
    fi

    # Only deploy for master branch
    if [ "${TRAVIS_BRANCH}" != "master" ]; then
        echo 'No artifacts will be deployed; not on a deployable branch'
        exit
    fi

    wget 'https://s3.amazonaws.com/travis-ci-gmbh/artifacts/stable/build/linux/amd64/artifacts'
    chmod +x artifacts
    ./artifacts upload "${RESULT_FILE}"
)
