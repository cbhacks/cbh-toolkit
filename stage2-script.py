import boto3
import io
import zipfile

s3 = boto3.client('s3')
db = boto3.client('dynamodb')

def get_package(bucket, channel):
    dbr = db.get_item(
        TableName='LatestFiles',
        Key={
            'Bucket': { 'S': bucket },
            'Channel': { 'S': channel }
        },
        ConsistentRead=True,
        ProjectionExpression='ObjectKey'
    )
    assert 'Item' in dbr
    assert 'ObjectKey' in dbr['Item']
    assert 'S' in dbr['Item']['ObjectKey']
    s3r = s3.get_object(
        Bucket=bucket,
        Key=dbr['Item']['ObjectKey']['S']
    )
    return zipfile.ZipFile(io.BytesIO(s3r['Body'].read()))

def lambda_handler(event, context):
    # Any changes in behavior of this function must be manually pushed to AWS!
    # Changes in the exec'd code do not need to be pushed to AWS.
    stage2_zip = get_package('intermediates.toolkit.cbhacks.com', 'stage2')
    new_globals = {}
    new_globals['event'] = event
    new_globals['context'] = context
    new_globals['stage2_zip'] = stage2_zip
    new_globals['__name__'] = 'cbh_invoked_from_lambda'
    exec(stage2_zip.read('stage2-script.py'), new_globals, new_globals)

out_zip = None

def handle_zip(zf, in_prefix='', out_prefix=''):
    for fi in zf.infolist():
        if not fi.filename.startswith(in_prefix):
            continue
        fi_name = out_prefix + fi.filename[len(in_prefix):]
        out_zip.writestr(fi_name, zf.read(fi))

def handle_package(bucket, channel, *args, **kwds):
    handle_zip(get_package(bucket, channel), *args, **kwds)

packages={}
packages[('intermediates.toolkit.cbhacks.com', 'stage2')] = None
packages[('builds.drnsf.cbhacks.com', 'appveyor-x86')] = {
    'out_prefix': 'drnsf/'
}
packages[('builds.crashedit.cbhacks.com', 'appveyor')] = {
    'out_prefix': 'CrashEdit/'
}
packages[('misc-tools.cbhacks.com', 'pcsx-hdbg-i686')] = {
    'out_prefix': 'pcsx-hdbg/'
}

def main():
    import datetime
    import binascii

    out_buffer = io.BytesIO()

    global out_zip
    out_zip = zipfile.ZipFile(out_buffer, mode='w', compression=zipfile.ZIP_DEFLATED)

    handle_zip(stage2_zip, in_prefix='content/')

    for k, v in packages.items():
        if v is None: continue
        handle_package(*k, **v)

    out_zip.close()
    out_data = out_buffer.getvalue()

    now = datetime.datetime.utcnow()
    out_name = 'cbh-toolkit-{:04}{:02}{:02}-{:02}{:02}{:02}-{:08X}.zip'.format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        binascii.crc32(out_data)
    )

    s3.put_object(Bucket='toolkit.cbhacks.com', Key=out_name, Body=out_data)

if __name__ == 'cbh_invoked_from_lambda':
    for record in event['Records']:
        assert 'dynamodb' in record
        assert 'Keys' in record['dynamodb']
        rec_keys = record['dynamodb']['Keys']
        assert 'Bucket' in rec_keys
        assert 'S' in rec_keys['Bucket']
        assert 'Channel' in rec_keys
        assert 'S' in rec_keys['Channel']
        if (rec_keys['Bucket']['S'], rec_keys['Channel']['S']) in packages:
            main()
            break

if __name__ == '__main__':
    global stage2_zip
    stage2_zip = get_package('intermediates.toolkit.cbhacks.com', 'stage2')
    main()
