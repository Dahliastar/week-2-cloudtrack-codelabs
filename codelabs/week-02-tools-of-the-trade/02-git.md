# Part 2: Git and GitHub workflow

## Mental model
`working directory` → `git add` → `staging area` → `git commit` → `local repo` → `git push` → `remote (GitHub)`

## Checkpoint 0: one-time setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Authenticate to GitHub with SSH keys or a personal access token. Passwords no longer work over HTTPS.

## Checkpoint 1: fork and clone
1. Click **Fork** on this repo on GitHub.
2. Clone **your fork**:
```bash
git clone <your-fork-url>
cd cloud-track-codelab
git remote add upstream <this-repo-url>
git remote -v
```

## Checkpoint 2: branch, change, commit
```bash
git checkout -b add-profile-<username>
mkdir -p members
# create members/<username>.md using templates/member-profile.md
git status
git add members/<username>.md
git commit -m "docs: add my profile"
git log --oneline
```

## Checkpoint 3: push and open a PR
```bash
git push -u origin add-profile-<username>
```
On GitHub, click **Compare & pull request**. Check that the base repository is the **upstream** repo, not your fork.

## Checkpoint 4: when things go wrong
```bash
git diff                 # what changed, unstaged
git restore <file>       # discard unstaged changes to a file
git restore --staged <file>   # unstage
git commit --amend       # fix the last commit message
```

## Think about it
1. What is the difference between `git fetch` and `git pull`?
2. Why work on a branch instead of `main`?
