## Creating your PRs

We all want to share and contribute to others' projects.
Let's learn how to cope with unmergeble PRs!

1. clone your fork of git_workshop.
2. remember the file you created in <a href="https://github.com/nadavwe/git_workshop#before-you-start">Before You Start</a>? please edit it a bit.
3. commit & push.

now, let's create a PR:
  1. go to your github repository, and on the right click pull Requests. 
  5. click New Pull Requests.
  6. you should see a sad red entry "Can't automatically merge. Don't worry, you can still create the pull request."
  7. create your PR anyway.

to solve this, we will add the remote repository and resolve the conflicts:
  6. to add the remote repository:
```bash
git remote add upstream git@github.com:nadavwe/git_workshop.git
```
  upstream is just a name! you can call the remote wahtever you like.
  6. look at the remotes with
```bash
git remote -v
```

