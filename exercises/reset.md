

### Playing with Git Reset

* create a a new repository (```git init``` in some (empty) directory) and create a base commit to start from - this will be our base commit.
* change the file and commit again.

each time now we are going to use another reset method.
please run ```git status``` and ```git log``` and ```cat file``` before and after each line to see the effect of each command.

please also notice that HEAD~ is the parent of the current commit. you can also specify a number ~2 is the commit's grandparent = the parent of its parent.
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
* git reset --soft HEAD~
* status & log && cat!

see how your commit has been removed. the index is just the same as it was, with the your change still there.
see also that your file has not changed!

* commit your change again








the git book again:
https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified



