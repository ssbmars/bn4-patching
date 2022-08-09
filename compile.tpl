load-plugins "plugins\"
game mmbn4
load-file-index "indexes\mmbn4bm-us.tpi"
read-text-archives "out\armips\bn4bm.gba" 

read-text-archives "bm_text.tpl" -p
write-text-archives "out\MEGAMANBN4BMB4BE_00.gba"
clear

