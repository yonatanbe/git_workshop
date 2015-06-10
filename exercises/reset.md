

### Playing with Git Reset
This exercise is meant to show you the working of git reset. it's a basic - "let's run and see" so try and see while you're doing it. =)


### Preliminaries 
* create a a new repository (```git init``` in some (empty) directory) and create a base commit to start from - this will be our base commit.
* change the file and commit again.

### Notes

##### watch the effects!
each time now we are going to use another reset method.
please run ```git status``` and ```git log``` and ```cat file``` before and after each reset flavour to see the effect of each command.

##### referencing HEAD's ancestry
HEAD~ is the parent of the current commit. you can also specify a number: ~2 is the commit's grandparent = the parent of its parent. sometimes you see HEAD^ - it is also the parent of the current commit. confused? you can read more about it [here](http://www.paulboxley.com/blog/2011/06/git-caret-and-tilde).

### soft reset
* status & log && cat!
* git reset --soft HEAD~
* status & log && cat!

see how your commit has been removed. the index is just the same as it was, with the your change still there.
see also that your file has not changed!

* commit your change again


### regular (=mixed) reset
* status & log && cat!
* git reset HEAD~
* status & log && cat!

see how your commit has been removed. also the index has changed as well, and now you have to include your file again.
see also that your file has not changed!

* ```git add``` your changes to the index and then commit again.

### hard reset
YOU ARE GOING TO LOSE DATA! (well, not really, see in a sec)
* status & log && cat!
* git reset --hard HEAD~
* status & log && cat!

see how your commit has been removed. The index has also changed. your changes to the file has been removed from your working directory as well.

### getting reset'd data back
git makes it unbelivebly difficult to lose commits, even if they have been reset'd, deleted, removed or whatever.
git by default save your commits 3 month, even if they are abandoned and cannot be accessed from other commits.
so let's get this commit back from the dead:
* ```git reflog```

reflog tells you where the head has been each time it was changed.
the first line is the current HEAD.
the second line is the commit that was before the current head - let's call this second hash ```<MY_SAVIOR>```.
* status & log && cat!
* ```git rebase <MY_SAVIOR>```
* status & log && cat!

see how your commit has been recovered. The index has also changed. your changes to the file has magically reappered as well.

#### Extra reading
[the git book again](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)



