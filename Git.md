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

## Remote repos

### basic bare repo

First, we set up a git user:

```bash
sudo adduser git
su git
cd ~ && mkdir .ssh && chmod 700 .ssh
touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
```

Then we append devs' keys into `authorized_keys` and then create the repo directory as follows, convention is to end the name with `.git`.

```bash
cd /some/dir
mkdir project.git
cd project.git
git init --bare
```

Now either clone the repo or add the repo as one of your remotes.

```bash
git remote add origin git@server:/some/dir/project.git
#or
git clone git@server:/srv/git/project.git
```

To secure the `git` user against abuse, prepend each key with following:

```no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty```

And change the shell preventing direct logins

```bash
cat /etc/shells   # see if git-shell is already in there. If not...
which git-shell   # make sure git-shell is installed on your system.
sudo -e /etc/shells  # and add the path to git-shell from last command
sudo chsh git -s $(which git-shell) #changes the gits shell to git-shell
```

## Sos for the stuff

- [Official Git website](https://git-scm.com/book/en/v2/)
- [Github tutorial](https://docs.github.com/en/get-started/quickstart)
- [GitHub cheat-sheet](https://training.github.com/downloads/github-git-cheat-sheet/)
- [Remove unsaved changes](https://stackoverflow.com/questions/14075581/git-undo-all-uncommitted-or-unsaved-changes)
- [Branching](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows) and [rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
- [Remote branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches)
- [changing remote url](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)
- [Setting up basic bare repo](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)
