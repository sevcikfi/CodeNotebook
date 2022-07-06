# Git quick info


## Basic setup

**TODO**: write
--system for /etc/, --global for HOME/~/.gitconfig and
--local in .git folder in your repo

### Basic setup (commit editor nano, default branch main):
```bash
git config --global user.name "name"
git config --global user.email "person@example.com"
git config --global core.ui auto
git config --global core.editor nano
git config --global init.defaultBranch main
```
For local repos to remember name and password/token:
```bash
git config --global credential.username
git config --global credential.helper store
```
To set VS Code as preferred git merge/diff:
```bash
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED

git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```
## How to start repo/pull from online host e.g. Github/Gitlab

TODO: ~~copy that for quick tut on GH~~

```bash
echo "# Your Repo Here" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin remote.repo.url.git
git push -u origin main
```

### Undo last commit

```bash
git push -f origin HEAD^:master
```

or 

```bash
git rebase -i HEAD~2
git push origin +branchName --force
```

or

```bash
git reset --hard HEAD^
git push origin -f
```

## Sos for the stuff

[Official Git website](https://git-scm.com/book/en/v2/),
[Github tutorial](https://docs.github.com/en/get-started/quickstart) and
[GitHub cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/)
