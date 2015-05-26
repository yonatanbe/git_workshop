# git workshop
a workshop on git - how to create your PRs so others can merge them easily.

## Before You Start
Because we want everyone to use the same repository, please do this before doing anything else:

1. Click the '+' sign where it says <a id="plus" href="#plus"><img src="https://github.com/nadavwe/git_workshop/raw/master/.readme/git_workshop_plus.png" width="100px" title="git_workshop/+" alt="git_workshop/+" align="center"/></a>. that will also create a fork for you.
1. give your file the name of your team (or any other identifying name of your choice). try to make it special so there won't be clashes. also write some text in your file.
2. now click <a id="pull" href="#pull"><img src="https://github.com/nadavwe/git_workshop/raw/master/.readme/create_pull_request.png" width="100px" title="create pull request" alt="create pull request" align="center"/></a>, and then click again on the bottom of the page.
3. you're finished! thanks for doing this first before anything else. =)

### the git book
https://git-scm.com/doc

great source for all git users, be it first timer or savvy.






### git internals
https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

to see object content:
```bash
git cat-file -p <object-hash>
```

to see raw object:
```bash
cat <git-object-file> | python -c "import sys;print repr(sys.stdin.read().decode('zip'))"
```


