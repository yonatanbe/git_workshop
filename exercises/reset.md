

### Playing with Git Reset

* create a a new repository (```git init``` in some (empty) directory) and create a base commit to start from - this will be our base commit.
* change the file and commit again.

each time now we are going to use another reset method.
please run ```git status``` and ```git log``` and ```cat file``` before and after each line to see the effect of each command.

#### a note on HEAD with tilde and caret
HEAD~ is the parent of the current commit. 

you can also specify a number: ~2 is the commit's grandparent = the parent of its parent.
sometimes you see HEAD^ - you can read more about it [here](http://www.paulboxley.com/blog/2011/06/git-caret-and-tilde).

#### soft reset
* status & log && cat!
* git reset --soft HEAD~
* status & log && cat!

see how your commit has been removed. the index is just the same as it was, with the your change still there.
see also that your file has not changed!

* commit your change again


#### regular (=mixed) reset
* status & log && cat!
* git reset HEAD~
* status & log && cat!

see how your commit has been removed. also the index has changed as well, and now you have to include your file again.
see also that your file has not changed!

* ```git add``` your changes to the index and then commit again.

#### hard reset
YOU ARE GOING TO LOSE DATA! (well, not really, see in a sec)
so do it in a dummy repository.
* status & log && cat!
* git reset --hard HEAD~
* status & log && cat!

see how your commit has been removed. also the index has changed as well and your changes to the file has been removed from you working directory as well.










the git book again:
https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified



