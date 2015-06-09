## Merging your PRs when conflicts arise

We all want to share and contribute to others' projects. but sometimes more than one person works on the same file and conflicts happen. regular conflicts in repositories are a bit easier to solve, but between repositories this can get strange...
So let's learn how to cope with unmergeble PRs!

#### Create a PR
* did you do the <a href="https://github.com/nadavwe/git_workshop#before-you-start">"Before You Start"</a>? If not, please fork this repository now!
* clone your fork of git_workshop into your computer.
* add a new file somewhere in the fork.
* commit & push.

now, let's create a PR:
* go to your github repository, and above the tree click Pull Request. 
* click create pull Request
* and then again - click the big green "create pull request" button.

#### Registering the repository where you forked from
this should only be done once for each new clone.
* add the remote repository:
```bash
git remote add upstream git@github.com:nadavwe/git_workshop.git
```
  upstream is just a name! you can call the remote whatever you like. if you have good ideas for names for forked repositories I'd love to hear, as origin is already taken. =/
* you can see what remotes are configured with
```bash
git remote -v
```


#### Rebasing your data locally
Let's bring the new data from the upstream repository:
* bring the new commits with 
```bash
git fetch upstream
```
this reads all the new objects (remember? blobs, trees, commits) from upstream to your local clone.

now we are ready to tackle the conflict:
* reveal the conflict with
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

#### Last Step! Force push your change
we're almost done! make sure you're happy with the current branch you have, because we are going to override whatever data you have on your forked repository!
force push your repository with
```bash
git push --force
```

go back to your PR and see that it's green and ready to be merged! congrats! =)





