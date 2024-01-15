# Z-COBOL-COMPILER
A simple, really bad, wrapper for gnucobol to compile script with dependent functions i made for myself while learning cobol.

It takes in info from `CompileCOBOL` file and creates and executes the compilation commands so you dont have to do them all individually

Its really unstable not recomended for use i use arch and it works on my pc 
## Usage
Make sure you have [gnucobol](https://archlinux.org/packages/extra/x86_64/gnucobol/) installed if you dont `yay -S gnucobol`

All you need is the `compile.py` file and you can run it to create a `CompileCOBOL` config file

After you fill out the `CompileCOBOL` config file run `compile.py` again and you will get the prompt `(extensions) has -x -o:` just hit enter and it will normally be good enough. The default extensions make it so the final file is an exicutable(-x) and it outputs to loacation(-o).



### Example CompileCOBOL file
```
#FIRST: OUTPUT PATH
#SECOND: SCRIPTS
#THIRD: NAME
#FORTH: MAIN FILE
#AFTER: FUNCTION FILES
./bin/
./Scripts/
TESTING
Main.cob
Function.cob
```
Any Line starting with # is excluded header is there to make it easier to remember what goes where
