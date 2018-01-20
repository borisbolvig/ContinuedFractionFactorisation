## Navigating Terminal

To use Terminal you will two basic commands for navigating.
In the Terminal you are always in some directory. Every directory has an address like /home/boris/documents/.
To see your current working directory, type in `pwd` and hit Enter.

To change directory type `cd` followed by a whitespace and the full or relative path to the new directory.

```
Boriss-MacBook-Pro:~ Boris$ pwd
/Users/Boris
Boriss-MacBook-Pro:~ Boris$ cd Documents
Boriss-MacBook-Pro:Documents Boris$ pwd
/Users/Boris/Documents
```


Another useful command is `ls`. This *lists* the files and subdirectories of the current work directory. 

Run 

```which python```

If you get something that is not an error message, you should be able to run the code.

Any .py file can be run by

```python anypyfile.py```

as long as that file is in the current work directory. (Otherwise specify the full or relative path to the file.)

## Continued Fraction Factorisation

You will have to modify the code slightly to get relevant response for different questions. The file of interest is that called "continued fraction factorisation.py". (Hint: If you start typing and hit TAB in the Terminal it will try to auto-complete. That way it will automatically sort the whitespaces in the filename for you. " " is replaced by "\ "  ...)

Everything after the line 

```if __name__=="__main__":```

will be executed when you run the script from the Terminal. 
So in this section you can comment/uncomment calls to functions like `Q2`, `Q3` that are relevant for respective questions. 
