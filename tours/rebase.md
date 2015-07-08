
### Interactive Rebasing
interactive rebase is a tool that helps you reshape the history of your commits.
in it's basic form it allows you to squash commits - from several commits create a single commit.

we will use here some notations that are covered in [Reset tour notes section](reset.md#notes). you can also reuse the repository you created there.

### Preliminaries
* create a new empty repository
* commit a file into the repository. this commit will be our base commit.
* now add another two commits - create new files, change the data in the commits - feel free, be wild!

great! we now have 3 commits - base commit, second commit, third commit.
```git log``` to some them all three in their glory.

### Basic Squash
* ```git rebase -i HEAD~2```
that will tell git to start interactive rebase on the last 2 commits.
look at the opened dialog and read the commands a bit.
now leave the editor with no changes.
* log & status
you'll see no change has been done to the file.



