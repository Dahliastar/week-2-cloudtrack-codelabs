# Week 2 Assignment

**Submit via PR to** `submissions/week-02/<your-github-username>/`.

## Task 1: First contribution (required)
Add your profile at `members/<your-github-username>.md` using [`templates/member-profile.md`](../../templates/member-profile.md). Open a PR.

## Task 2: Linux script (required)
Write `organize.sh` that takes a folder and sorts its files into subfolders by extension (`.txt` → `txt/`, `.png` → `png/`). Include a short `NOTES.md` explaining how to run it.

## Task 3: Containerize a tiny web app (required)
Write a small web app in any language (it can be a different one from the lab), plus a `Dockerfile`. In `NOTES.md`, include:
- the exact build and run commands
- the output of `curl localhost:<port>`
- the cleanup commands you ran

## Stretch goals (optional)
- Add a `.dockerignore` and explain what it does
- Use a smaller base image and compare sizes with `docker images`
- Make the container run as a non-root user

## Submission checklist
- [ ] Profile PR opened
- [ ] `organize.sh` runs without errors
- [ ] Docker image builds from a clean clone
- [ ] No secrets committed
- [ ] Container and image cleaned up locally

## Deadline
Before the Week 3 session (confirm date in the track channel).
