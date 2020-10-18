![](./images/Steg1.bmp)
# **1. binwalk**
```
$ binwalk -B Steg1.bmp

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PC bitmap, Windows 3.x format,, 1280 x 826 x 24
2889608       0x2C1788        VMware4 disk image
```
# **2. exiftool**
```
$exiftool Steg1.bmp

ExifTool Version Number         : 12.06
File Name                       : Steg1.bmp
Directory                       : CSCI17/wargames/NCL/crypto/Steg1/images
File Size                       : 3.0 MB
File Modification Date/Time     : 2020:10:17 20:19:40-07:00
File Access Date/Time           : 2020:10:17 20:19:40-07:00
File Inode Change Date/Time     : 2020:10:17 20:19:40-07:00
File Permissions                : rw-r--r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Windows V3
Image Width                     : 1280
Image Height                    : 826
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 3171840
Pixels Per Meter X              : 0
Pixels Per Meter Y              : 0
Num Colors                      : Use BitDepth
Num Important Colors            : All
Image Size                      : 1280x826
Megapixels                      : 1.1
```

# **3. Nothing found using stegsolve.**

