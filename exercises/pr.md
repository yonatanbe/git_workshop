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

to solve this, we will add the remote repository and resolve the conflicts:
* add the remote repository:
```bash
git remote add upstream git@github.com:nadavwe/git_workshop.git
```
  upstream is just a name! you can call the remote whatever you like. if you have good ideas for forked repositories I'd love to hear, as origin is already taken. =/
* look what remotes are configured with
```bash
git remote -v
```

