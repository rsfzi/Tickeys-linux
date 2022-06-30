#!/bin/bash
pyinstaller build32.spec
cd ./tickeys/locale
chmod +x gen_mo.sh
./gen_mo.sh
