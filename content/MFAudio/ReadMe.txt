
=======================
MFAudio v1.1 ReadMe.TXT
=======================

Email: muzzleflash@emaildownunder.com
Web: http://muzzleflash.da.ru


Welcome to MFAudio
------------------

This tool allows you to play, convert, and downsample audio files that use some of the more common formats among PS2 games.

It can be used to reduce the size of music in DVD rips, replace the music with something else you prefer, or simply to play the music from your favorite games.

Please note: It is assumed that the user has a reasonable level of technical knowledge - this tool isn't for newbies. Please *do not* email me questions about how to play/convert a file from a particular game. You're on your own!

Usage
-----

Using the GUI should be straight-forward. Press the 'Open' button and select the file you wish to use as input. If the file is a known format, then all the details will be automatically filled in. Otherwise, the format will default to Raw (uncompressed or compressed), and you will likely need to set the frequency, channels, and interleave manually. The 'offset' option can be used to step past a certain number of bytes that may exist at the start of the file prior to the audio data. You can use the 'Play' button to test the settings and determine if they are correct.

Creating an output file for conversion should be just as easy. Start by selecting the output format, and then give a filename. The frequency, channels, and interleave will all default to the same as the input file, so you only need to change them if you intend to downsample.

You can also use the utility from the command line (type 'MFAudio /?' for available options). This can be useful if you are creating a rip kit, for example, you can write a batch file that will run this utility to downsample all the music in the game.

Restrictions
------------

Not supported: 
 * MUS & MPC formats (used mainly in EA games)
 * AFS format (used mainly in Sega Dreamcast ports)

Examples
--------

Here are some settings to play/convert the music from a few different games. I've noted the region I used for testing (PAL, NTSC, NTSC-J).

Airblade (PAL)
  \L0\*.VAG, \L1\*.VAG, \L2\*.VAG, \L3\*.VAG, \L4\*.VAG, \L5\*.VAG,
  \L6\*.VAG: Raw Compressed, Freq 44100, Channels 2, Interleave 10

ATV Offroad Fury (NTSC)
  \RES\SONG*.L,
  \RES\SONG*.R: VAG Format (built-in support).
  Note: L is left channel, R is right channel.

Batman Vengeance (NTSC)
  \GAMEDATA\WORLD\SOUND\STRM.SM1: Raw Compressed, Freq 44100, Channels 2, Interleave 800

Bloody Roar 3 (NTSC)
  \STR\M*.PCM: Raw Uncompressed, Freq 48000, Channels 2, Interleave 200

Burnout (PAL)
  \*.VAG: Raw Compressed, Freq 44100, Channels 2, Interleave 10

Cart Racing Fury (PAL)
  \SOUND\*.WAV: WAV Format (built-in support).

Crazy Taxi (NTSC)
  \RES\ADS\MUSIC.STR: Raw Compressed, Freq 44100, Channels 2, Interleave 4000
      Offset      800,   5E8800,   7E8800,   908800,  1258800,  1998800,
              2288800,  29A0800,  29F8800

Dave Mirra Freestyle BMX 2 (PAL)
  \ASSETS\AUDIO\MUSIC.ZSD: Raw Compressed, Freq 48000, Channels 2, Interleave 800
      Offset      800,   C21800,  16A5800,  22AA800,  2E9B800,  3E3B800,
              4CDD800,  5494800,  5DBC800,  65E7800

Devil May Cry (NTSC)
  \DATA\ADS\BATTLE.XAG: Raw Compressed, Freq 44100, Channels 2, Interleave 4000
      Offset        0,   3C0000,   758000,   A10000,   E60000,  1108000,
              1328000,  15B8000,  1970000,  2028000,  22A8000,  2718000,
              2A80000,  2C60000,  3050000,  32D0000,  34D0000,  3640000,
              39F8000,  3C20000,  3DE0000,  41C8000,  44E0000,  47A8000,
              4880000,  4B50000,  4E20000,  4F00000,  4FD0000,  5328000,
              5450000

Donald Duck (NTSC)
  \GAMEDATA\WORLD\SOUND\STREAMED.BLK: Raw Compressed, Freq 44100, Channels 2, Interleave 800

Doukyu Billiards (NTSC-J)
  \BGM\*.SWV: Raw Uncompressed, Freq 48000, Channels 2, Interleave 200

Driving Emotion Type-S (PAL)
  \DATA\BGM*.BIN: Raw Compressed, Freq 48000, Channels 2, Interleave 2000, Offset 10

Dropship (PAL)
  \MUSIC.WAD: Raw Compressed, Freq 44100, Channels 1
      Track 1: Left - Offset 840        Right - Offset 6E5840
      Track 2: Left - Offset DCA840     Right - Offset 15AC040
      Track 3: Left - Offset 1D8D840    Right - Offset 26A2840
      Track 4: Left - Offset 2FB7840    Right - Offset 3391840
      Track 5: Left - Offset 376B840    Right - Offset 3B17840
      Track 6: Left - Offset 3EC3840    Right - Offset 41B2840
      Track 7: Left - Offset 44A1840    Right - Offset 48AA040
      Track 8: Left - Offset 4CB2840    Right - Offset 4EC1040
      Track 9: Left - Offset 50CF840    Right - Offset 5438840
      Track10: Left - Offset 57A1840    Right - Offset 5D31840
      Track11: Left - Offset 62C1840    Right - Offset 68AA840
      Track12: Left - Offset 6E93840    Right - Offset 720F840
      Track13: Left - Offset 758B840    Right - Offset 78A1840
      Track14: Left - Offset 7BB7840    Right - Offset 7C16040
      Track15: Left - Offset 7C74840    Right - Offset 7CCE840
      Track16: Left - Offset 7D28840    Right - Offset 821C040
      Track17: Left - Offset 870F840    Right - Offset 8A8A040
      Track18: Left - Offset 8E04840    Right - Offset 9180840

Dynasty Warriors 2 (PAL)
  \BGM.BNS: Raw Compressed, Freq 44100, Channels 2, Interleave 10
      Offset      800,   3EF800,   88D800,   C7E000,   FAD800,  13F8000,
              1867000,  1C40000,  209A800,  24CB000,  2970000,  2FD4800,
              32A8000,  32F7800,  33FF000,  3485000,  34C7800,  38BD000,
              3C69000

Dynasty Warriors 3 (NTSC)
  \BGM.BNS: Raw Compressed, Freq 44100, Channels 2, Interleave 10
      Offset      800,   44B000,   995000,   DE6800,  122A800,  175F800,
              1C56000,  21E3800,  2754800,  2B77000,  3018800,  3527000,
              3BBE000,  4416000,  4A30800,  5150000,  5688800,  5E09800,
              62CC000,  6679000,  6BB8800,  6E86800,  7383000,  77F0800,
              7CB4000,  7E95800,  82B8000,  86D7000,  8F5D000,  916E000,
              95AD000,  9AF8000,  9B80000,  9BD4000,  9C12800,  9C9D800,
              9CD2800

Extermination (PAL)
  \STREAM\MUSIC.DAT: Raw Compressed, Freq 48000, Channels 2, Interleave 400
      Offset        0,   B24000,  1583000,  1DE4000,  27A7000,  330C000,
              3EAF000,  483F000,  5C9D000,  6ABE800,  6FD0000,  73D9000,
              787CC00,  7887000,  78F3000,  7979800,  7EF0800,  843D800,
              8A68800,  8F22800,  9387000,  96A9000,  99D3000,  9A43400

Extreme G3 Racing (PAL)
  \MUSIC\FLY*.XA2,
  \MUSIC\FRONTEND.XA2,
  \MUSIC\PION.XA2,
  \MUSIC\REPLAY.XA2,
  \MUSIC\VERDE.XA2: Raw Compressed, Freq 44100, Channels 2, Interleave 1000, Offset 800
   * All other XA2 files in MUSIC directory cannot be played correctly with MFAudio

Fantavision (NTSC-J)
  \DATA\BGM\BGM*.INT: Raw Uncompressed, Freq 48000, Channels 2, Interleave 200

Formula One 2001 (PAL)
  \STREAM\MUSIC\*.PCM: Raw Uncompressed, Freq 48000, Channels 2, Interleave 0
  \STREAM\MUSIC\STR*.PCM: Raw Uncompressed, Freq 24000, Channels 2, Interleave 0

Gauntlet: Dark Legacy (NTSC)
  \WAD.BIN: Raw Compressed, Freq 24000, Channels 2, Interleave 20
      Offset  E6C9028,  E866028,  ED6C828,  EDAD028,  F2B6028,  F5F1828,
              FC14028, 10300828, 1096D828, 10F8A828, 1216F828, 1266B828,
             12762828, 128FF828, 12A6D828, 12B8C028, 12D3E028, 1309A828,
             13482828, 1385C028, 13B2C828, 13EB5028, 13EDD828, 142E2028,
             144D8828, 144E1028, 1478B028, 14B2B828, 14CD8028, 14EF0028,
             151B9828, 1538D828, 15562028, 1572E828, 159A6828, 15D74828,
             1608C828, 1665E028, 168B3828, 168CB028, 168FE828, 16D0B028,
             16D83828, 17030028, 17334028, 17CE8828, 17E49828, 17E73828,
             17FB1028, 18103828, 182D1828, 184C2028, 18621028, 1879D028,
             18971028, 18FB0028, 19063028, 190E9028, 191E1028, 1940F828,
             1948C028, 1954F028, 196E1028, 1978E828, 19841828, 19879828,
             1A643028, 1A7EA828, 1A8BA828, 1A8E6828, 1A93E828, 1AD40028,
             1B478028, 1B750828, 1BB3E828, 1C017028, 1C32E828, 1C668828
  \WAD.BIN: Raw Compressed, Freq 24000, Channels 1
      Offset 11491028, 11A60028, 11BE9028, 11DEC828, 11FEF028, 12EFA028,
             12F53828, 12FBA028, 1301E828, 174FC028, 1776C828, 17A8F028,
             17C39028, 198BC828, 19A40028, 19A4F028, 19A63828, 19A7F028,
             19CA8028, 19EA6028, 19F75028, 19F86028, 1A061028, 1A0F2028,
             1A183028, 1A195828, 1A250828, 1AC62828, 1AD32828, 1B0EC028,
             1B26A028

Gradius (PAL)
  \SD\G0_BGM: Raw Compressed, Freq 44100, Channels 2, Interleave 4000
  \SD\G3_BGM*: Raw Compressed, Freq 44100, Channels 1
  \SD\G4_BGM*: Raw Compressed, Freq 44100, Channels 2, Interleave 4000

Gran Turismo 3 (All Versions)
  \BGM\*.ADS: SS2 Format (built-in support)
   * Grab Zandal's GT3.VOL extractor (http://www.geocities.com/zandal73/Zindex.html) in order to extract the music files from the GT3.VOL archive

Grand Theft Auto 3 (NTSC)
  \AUDIO\MUSIC\CHAT.VB: Raw Compressed, Freq 16000, Channels 2, Interleave 2000
  \AUDIO\MUSIC\*.VB: Raw Compressed, Freq 32000, Channels 2, Interleave 2000

Gungriffon Blaze (PAL)
  \MUSIC\GG3.STZ: STZ Format (built-in support)

Internation Track & Field (PAL)
  \SOUND\BGM.VAS: VAS Format (built-in support)

ISS (PAL)
  \SOUND\BGM.VAS: VAS Format (built-in support)

Kessen 2 (NTSC)
  \LINKDATA.ANS: Raw Compressed, Freq 44100, Channels 2, Interleave 10
      Offset 418AC800, 419AC800, 419EF000, 41BCE800, 41C30800, 41C92800,
             41CEF800, 41E72800, 41F75000, 42055000, 42214800, 423D2000,
             42588000, 4274C800, 42B7F000, 42E9A000, 430EE000, 434AC000,
             43927800, 43D83800, 441B1000, 44616800, 44A88000, 44E24000,
             4503D800, 4507B000, 45227800, 45271000, 452E9000, 45676800,
             456DB000

Maximo (NTSC)
  \PSXDATA\MUSIC\*.VGM: Raw Compressed, Freq 44100, Channels 2, Interleave 6280

MX 2002 (PAL)
  \STREAMS\STRM*.STR: Raw Compressed, Freq 44100, Channels 2, Interleave A000

NBA2Night (NTSC)
  \SOUND\DATA\STRBGM.VAS: VAS Format (built-in support)

Ring of Red (NTSC)
  \BGM\*.RAW: Raw Uncompressed, Freq 24000, Channels 2, Interleave 0

Rune: Viking Warlord (PAL)
  \MUSIC\THMMUSIC\THEME\SNGTHM*.VGV: Raw Compressed, Freq 22050, Channels 1

Shadow Man: 2nd Coming (PAL)
  \PS2DATA.BIN: Raw Compressed, Freq 22050, Channels 2, Interleave 3000
      Offset    B2800,   5B7000,   A5B800,   AF8000,   B70800,   C01000,
              111D800,  12DA000,  1352800,  147F000,  196B800,  1B28000,
              2050800,  25CD000,  28B5800,  29BE000,  2AAE800,  3133000,
              3157800,  3470000,  395C800,  3C21000,  3FD5800,  450A000,
              4A32800,  4D9F000,  4EEF800,  5514000,  5A84800,  5AE5000,
              60B5800,  63B6000,  64E2800,  6B2B000,  6F6F800,  6F94000,
              6FB8800,  7265000,  7589800,  75EA000,  7A82800,  7CFF000,
              7D53800,  81B0000,  8780800,  8A39000,  8ABD800,  8B12000,
              8B7E800,  8CE7000,  9263800,  9708000

Silent Scope (PAL)
  \BGM\*.RAW: Raw Uncompressed, Freq 24000, Channels 2, Interleave 0

Silent Scope 2 (NTSC)
  \DATA\SD.BIN: Raw Compressed, Freq 44100, Channels 2, Interleave 2000
      Offset   61A800,   7D7800,   9DA800,   A1F800,   CCF800,   FB2800,
              1198800,  1854000,  1C42800,  1E2F800,  1ECF800,  20E9000,
              222A000,  24F5000,  27D8000,  280E800,  295A800,  29E9800,
              2DAB000,  3006000,  3324000,  36F0000,  3976800,  3CC9800,
              3D3B800,  3F97800,  43A7800,  46DA000,  4D14000

Silpheed (NTSC-J)
  \SOUND\SIL.STZ: STZ Format (built-in support)

Star Wars: Jedi Starfighter (NTSC)
  \STREAMS.PAK: Raw Compressed, Freq 44100, Channels 2, Interleave 40
      Offset 1178B900, 11A32100, 11C29900, 11F8C100, 1221B100, 1249D900,
             12737900, 129CD100, 12D6C900, 12F80100, 132A9100, 1353F900,
             13714100, 139BA900, 13C77100, 13F3C900, 14186900, 143B5900,
             14755100, 14926100, 14CA0100, 14F35900, 151CD900, 1544A100,
             15694100, 1592E100, 15D49100, 16222900, 1685E900, 16D0E900,
             173C9900

Star Wars: Starfighter (NTSC)
  \STREAMS\MUSIC\*.SCX: Raw Compressed, Freq 24000, Channels 2, Interleave 40, Offset 100

Star Wars: Super Bombad Racing (PAL)
  \MUSICPS2.DAT: Raw Compressed, Freq 24000, Channels 1
      Track 1: Left - Offset 44         Right - Offset 104CC4
      Track 2: Left - Offset 209944     Right - Offset 30EC24
      Track 3: Left - Offset 413F04     Right - Offset 433F24
      Track 4: Left - Offset 453F44     Right - Offset 582124
      I'll leave the rest to you...

Surfing H3O (PAL)
  \GZMVS.RBB: Raw Compressed, Freq 48000, Channels 2, Interleave 2000
      Offset     1000,    BD000,   1C5000,   3C1000,   5B9000,   819000,
               A81000,   D2D000,   FD1000,  12ED000,  1695000,  1CC9000,
              2481000,  2E4D000,  3855000,  4049000,  4A8D000

Thunderhawk: Operation Phoenix (PAL)
  \MUSIC\*.P2A: Raw Uncompressed, Freq 44100, Channels 2, Interleave 200

Time Crisis 2 (NTSC)
  \FGI.BIN: Raw Compressed, Freq 44100, Channels 2, Interleave 400
      Offset    63800,   232400,   834000,   CDF800,  1142000,  157F800,
              1B39000,  202A800,  23B7000,  25F6800,  2A64000,  2C55000,
              2F8D800,  3193000,  35D2800,  386D000

TimeSplitters (PAL)
  \MUSIC\*.MSC: Raw Compressed, Freq 44100, Channels 2, Interleave 8000

Tokyo Extreme Racer Zero (NTSC)
  \SMC\MUSIC.SMC: Raw Compressed, Freq 48000, Channels 2, Interleave 8000
      Offset        0,   360000,   600000,   8A0000,  1380000,  16C0000,
              1E00000,  28A0000,  32E0000,  37C0000,  3CC0000,  41C0000,
              46A0000,  4BA0000,  50A0000,  55A0000,  5A80000,  5F00000,
              63E0000,  68E0000,  6DC0000,  72A0000,  7760000,  7C40000,
              8120000,  81A0000,  8240000,  8900000,  9540000,  A180000,
              ABC0000,  B5C0000

Tony Hawk Pro Skater 3 (NTSC)
  \MUSIC\MUSIC.WAD: Raw Compressed, Freq 44100, Channels 2, Interleave 18000
      Offset        0,   AB0000,  1440000,  1DA0000,  2430000,  2E20000,
              3810000,  4260000,  4EF0000,  59A0000,  6570000,  6BD0000,
              7200000,  7DA0000,  8A00000,  95A0000,  9FF0000,  A890000,
              B4F0000,  C1E0000,  C8D0000,  D4D0000,  E040000,  E8B0000,
              F0C0000,  FA20000, 105F0000, 112B0000, 11790000, 12360000,
             12DB0000, 139E0000, 14160000, 144F0000

Top Gear Dare Devil (PAL)
  \SOUND\*.VAG: VAG Format (built-in support).

Top Gun: Combat Zones (NTSC)
  \DATA\SOUND\BGM\*.WAV: WAV Format (built-in support).

Twisted Metal Black (NTSC)
  \VAG\*.VAG: VAG Format (built-in support).

Unreal Tournament (NTSC)
  \MUSIC\*.VGM: Raw Compressed, Freq 22050, Channels 2, Interleave 10

The Weakest Link (PAL)
  \SOUND\STREAM\MUSIC\*.VAG: VAG Format (built-in support).

Wild Wild Racing (PAL)
  \MUSIC\*.VB: Raw Compressed, Freq 44100, Channels 2, Interleave 2000

Winter-X Games (PAL)
  \SOUND\BGM.VAS: VAS Format (built-in support)

Wizardry (NTSC)
  \PACKDATA.CIG: Raw Compressed, Freq 44100, Channels 2, Interleave 100
      Offset 1830E800, 187C3000, 19175800, 1976E000, 19EA0800, 1A458000,
             1AA6F000, 1B0DE000, 1B795800, 1BB3B800, 1BEF5800, 1C33D800,
             1C8AD800, 1CEFA800, 1D514000, 1D88A000, 1DDC1000, 1E215000,
             1E712800, 1EB0C800, 1EEE7000, 1F33B000, 1F754800, 1FA12000

WWF Smackdown: Just Bring It (NTSC)
  \ADS\0\*.ADS, \ADS\1\*.ADS, \ADS\2\*.ADS: SS2 Format (built-in support).

X-Squad (PAL)
  \SOUND\*.INT: Raw Uncompressed, Freq 48000, Channels 2, Interleave 200


Thanks & Greets...
------------------

Everyone associated with PS2 dev & ripping - in no particular order:
Paradox, Dynamite, Kalisto, Static, Z and the guys at PS2Ownz forums, Zandal, Toshi, PS2foryou.de, Hurricane, Bitmaster, and anyone I missed out!

Legal
-----

PSX, PS2, Playstation, Playstation2, are registered trademarks of Sony Computer Entertainment, Inc. This product is not sponsored, endorsed, or approved by Sony.

Everything here was written personally. It does not contain any copyrighted material (Sony or otherwise). 

Distribute as much as you like!
