# Challenge: The Broken Container

We will solve this together in the session, in pairs. **Do not look at hints until you have tried.**

## Scenario
A teammate handed you a web app and a Dockerfile and said "it works on my machine". It does not work in a container. Find and fix **every** problem.

## Your goal
```bash
cd challenges/week-02-broken-container
docker build -t broken-app .
docker run -d -p 5000:5000 --name broken broken-app
curl localhost:5000        # should print: It finally works!
```

## Rules
- Work in pairs. One drives, one navigates, swap every 10 minutes.
- Write down each bug you find and how you found it in `SOLUTION_NOTES.md`.
- Open a PR with your fixes to `submissions/week-02/<username>/broken-container/`.

## Bonus
- Add a `/health` endpoint returning `ok`
- Add a `.dockerignore`

## Hints (reveal one at a time)
<details><summary>Hint 1</summary>Read the error from `docker build` carefully. Which file does it say is missing?</details>
<details><summary>Hint 2</summary>The container is running but curl fails. What address is the app listening on?</details>
<details><summary>Hint 3</summary>Does the port in the code match the port you map with <code>-p</code>?</details>
