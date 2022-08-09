## place ROMs in `/rom/`
File names matter.  
bn4bm.gba  
bn4rs.gba  
To modify an additional rom, new parameters for it must be included in `compile.bat` and `compile.tpl`. If you are making assembly 

## finding the text archives to edit
There are full text archive dumps of BlueMoon and RedSun in `/textdumps/`. Search through it for what you want and copy the text to `bm_text.tpl` before editing. Some common text archives have already been copied over.  
An intact text archive looks like this:  
``` 
@archive 00A455
@size 10

script 0 mmbn4s {
	"Bingus"
	end
}
script 1 mmbn4s {
	"Binted"
	end
}
```
When copying a text archive, not all scripts need to be included. Any script that gets excluded will simply remain unmodified.  

## Sources
TextPet <https://github.com/Prof9/TextPet> (MIT License)  
armips <https://github.com/Kingcom/armips> (MIT License)  
Flips <https://github.com/Daedalus007/Flips-daedalus> (GPL3 License)  