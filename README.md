Description
===========

This repository holds signatures and plugins for
[``binwalk``](https://github.com/devttys0/binwalk) I wrote while analyzing
Samsung S6's proprietary bootloader
([article](https://blog.quarkslab.com/reverse-engineering-samsung-s6-sboot-part-ii.html)).

Usage
=====

Find and Extract MobiCore Load Format (MCLF) Files
--------------------------------------------------

```bash
$ mkdir -pv $HOME/.config/binwalk/{magic,plugins}
$ cp magic/mclf $HOME/.config/binwalk/magic/
$ cp plugins/mclf.py $HOME/.config/binwalk/plugins/
```

If you are using a version of ``binwalk`` anterior to [this
commit](https://github.com/devttys0/binwalk/commit/2051757c7b1ada4beb3c04454fd5a218334a35e9),
create the following symbolic link:

```
$ ln -sf ls -sf $HOME/.config/binwalk/ $HOME/.binwalk
```

Then, run ``binwalk`` as usual:

```
$ binwalk -D 'mobicore mclf' sboot.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
567696        0x8A990         SHA256 hash constants, little endian
674200        0xA4998         Android bootimg, kernel size: 0 bytes, [...]
677839        0xA57CF         POSIX tar archive, owner user name: [...]
1413120       0x159000        MobiCore Load Format, version 2.5
1478996       0x169154        SHA256 hash constants, little endian
1486848       0x16B000        MobiCore Load Format, version 2.5
```


Find ARMv7 Interrupt Vector Table
---------------------------------

```bash
$ binwalk -m magic/armel sboot.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1110016       0x10F000        ARMv7 Interrupt Vector Table, Little Endian
1110020       0x10F004        ARMv7 Interrupt Vector Table, Little Endian
1110024       0x10F008        ARMv7 Interrupt Vector Table, Little Endian
1110028       0x10F00C        ARMv7 Interrupt Vector Table, Little Endian
1110032       0x10F010        ARMv7 Interrupt Vector Table, Little Endian
1110080       0x10F040        ARMv7 Interrupt Vector Table, Little Endian
1110084       0x10F044        ARMv7 Interrupt Vector Table, Little Endian
1110088       0x10F048        ARMv7 Interrupt Vector Table, Little Endian
1110092       0x10F04C        ARMv7 Interrupt Vector Table, Little Endian
1110096       0x10F050        ARMv7 Interrupt Vector Table, Little Endian
1114080       0x10FFE0        ARMv7 Interrupt Vector Table, Little Endian
```
