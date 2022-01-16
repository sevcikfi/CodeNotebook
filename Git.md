# Git quick info


## Basic setup

**TODO**: write
--system for /etc/, --global for HOME/~/.gitconfig and
--local in .git folder in your repo

### Basic setup (commit editor nano, default branch main):
```
git config --global user.name "name"
git config --global user.email person@example.com
git config --global core.ui auto
git config --global core.editor nano
git config --global init.defaultBranch main
```
For local repos to remember name and password/token:
```
git config --global credential.username
git config --global credential.helper store
```
To set VS Code as preferred git merge/diff:
```
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED

git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```
## How to start repo/pull from online host e.g. Github/Gitlab

copy that for quick tut on GH

## Sos for the stuff

[Official Git website](https://git-scm.com/book/en/v2/),
[Github tutorial](https://docs.github.com/en/get-started/quickstart) and
[GitHub cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/)
