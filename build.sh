#!/bin/bash
pyinstaller build.spec
cd ./tickeys/locale
chmod +x gen_mo.sh
./gen_mo.sh
