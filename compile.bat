@echo off

armips build.asm -strequ GameNum bn4 -strequ GameName bm
echo finished armips
sleep 1

textpet run-script compile.tpl

flips -c -b "rom/bn4bm.gba" "out/MEGAMANBN4BMB4BE_00.gba" "out/MEGAMANBN4BMB4BE_00.bps"

timeout 2