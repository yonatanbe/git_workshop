## Creating your PRs

We all want to share and contribute to others' projects.
Let's learn how to cope with unmergeble PRs!

* clone your fork of git_workshop.
* remember the file you created in <a href="https://github.com/nadavwe/git_workshop#before-you-start">Before You Start</a>? please edit it a bit.
* commit & push.

now, let's create a PR:
  * go to your github repository, and on the right click pull Requests. 
  * click New Pull Requests.
  * you should see a sad red entry "Can't automatically merge. Don't worry, you can still create the pull request."
  * create your PR anyway.

we have a conflict! let's resolve it.

first, let's bring the new data from the upstream repository:
* add the remote repository:
```bash
git remote add upstream git@github.com:nadavwe/git_workshop.git
```
  upstream is just a name! you can call the remote whatever you like. if you have good ideas for forked repositories I'd love to hear, as origin is already taken. =/
* look what remotes are configured with
```bash
git remote -v
```
* bring the new commits with 
```bash
git fetch upstream
```
this reads all the new objects (remember? blobs, trees, commits) from upstream to your local clone.

now we are ready to tackle the conflict:
* create the conflict with
```bash
git rebase upstream/master
```
basically, we ask git to take the commits in upstream/master and have our commits on top of it.
git will tell you immediately that there is a conflict.
read the text it prints! it can help you understand what to do next.
* run ```git status``` - more information on what you can do. READ! ask questions if you don't understand!
* solve the conflict (your choice of solution). after you're happy with the file you have, add it to the index and continue the rebase. 
```bash
git add <file>
git rebase --continue
```





