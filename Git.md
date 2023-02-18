# Git quick info

## Basic setup

TODO: write
--system for /etc/, --global for HOME/~/.gitconfig and
--local in .git folder in your repo

### Basic setup (commit editor nano, default branch main)

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
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

### How to add remote

```bash
echo "# Your Repo Here" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main # renames current branch to main
git remote add origin remote.repo.url.git
git push -u origin main
```

### Undo last commit and push it to remote

All of following are *equally* correct.

```bash
git push -f origin HEAD^:master
```

```bash
git rebase -i HEAD~2
git push origin +branchName --force
```

```bash
git reset --hard HEAD^
git push origin -f
```

### Undo uncommitted/unsaved changes

This will unstage all files you might have staged with git add. Add `--hard HEAD` if you're in a subdirectory.

```bash
git reset
```

This will revert all local uncommitted changes (should be executed in repo root). If you want to unchange particular files, specify the file instead of the dot.

```bash
git checkout .
```

This will remove all local untracked files, so only git tracked files remain:

```bash
git clean -fdx
```

**WARNING**: -x will also remove all ignored files, including ones specified by .gitignore! You may want to use `-n` for preview of files to be deleted.

## Sos for the stuff

- [Official Git website](https://git-scm.com/book/en/v2/)
- [Github tutorial](https://docs.github.com/en/get-started/quickstart)
- [GitHub cheat-sheet](https://training.github.com/downloads/github-git-cheat-sheet/)
- [Remove unsaved changes](https://stackoverflow.com/questions/14075581/git-undo-all-uncommitted-or-unsaved-changes)
