## outline for swc: novice: shell  

#####Commands to cover:  
- `whoami`
- `pwd`
- `cd` -- go through this carefully: `..`, root, path
- `ls` options: `-a, -s, -l, -h, -r, -F`
- `man`, `help`, `apropos`  -- this isn't listed by swc, but I find it invaluable. If only for knowing what the various options mean. 
- `mkdir`  -- make a directory called `bootcamp` -- use it for your work
- `mv`
- `cp`
- `rm`  *!!!! give warnings !!!!* there is no trashbin
- `rmdir` -- but doesn't work unless empty, so `rm -r` is useful but dangerous.


Looking inside files: 
  
- `nano` -- basic editor (NOT Word Processors!)  
- `head`  
- `tail`  
- `cut`  
- `sort`  
- `cat`  

Control:


#####Concepts to cover: 
- The file system: make a figure and use it!
 	- folders
 	- files
 	- name.ext -- what's an extension? why is it there?
 	- paths
 		- relative paths (`..`, `.`)
 		- absolute paths (`/usr`, different uses of `/`)
- working with the file system:
 	- shell = command line interpreter = REPL -
 	- a command is a program 	
 	- case-sensitive: `ls -f` is not the same as `ls -F`
 	- BASH = 'Bourne Again Shell' -- there are others (wikipedia/en/CLI)
 	- create, delete, edit, rename, copy, etc. what do you do with your file system?
 	- what do you _wish_ you could do with your file system?
- Dangers of deletion on unix:  there is no going back
- Redirection: `>, >>, <, |`

 	
####Carpentry to cover:
- Thoughtful names: Set yourself up to find things easily
	- confName_year
		- data
		- paper
		- analysis
		- images
	- maintain unique data names from sources.
- Get the computer to do it (especially if tedious, repetitive) 		A form of DRY: don't repeat yourself
- Add comments: It's only re-usable if you know what it does.
- Simple pieces build powerful processes
	