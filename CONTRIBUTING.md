# Contributing

## Submitting an assignment

```bash
git clone <your-fork-url>
cd cloud-track-codelab
git remote add upstream <this-repo-url>
git checkout -b week-02-<your-github-username>
mkdir -p submissions/week-02/<your-github-username>
# add your work, then:
git add .
git commit -m "week-02: submission from <your-github-username>"
git push -u origin week-02-<your-github-username>
```

Open a PR **against the upstream repo's `main`**, not your own fork.

## Rules of the road

- Only touch your own folder under `submissions/`. This avoids merge conflicts.
- One PR per assignment. Fill in the PR template.
- Never commit secrets, tokens, keys or `.env` files. If you do, tell a lead immediately and rotate the secret.
- Use [Conventional Commits](https://www.conventionalcommits.org/): `docs:`, `feat:`, `fix:`, `chore:`.
- Be kind in reviews. Explain the why, not just the what.

## Keeping your fork current

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

## Proposing a new codelab or challenge

Copy a file from `templates/`, fill it in, and open a PR. Leads review for accuracy and difficulty.
