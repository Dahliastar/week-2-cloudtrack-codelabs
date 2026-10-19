# Lab 6: Ship it to the cloud (self-paced or follow-up session)

Goal: turn your image into a public URL.

## Option A: Google Cloud Run (recommended)

Prerequisites: a Google Cloud project with billing enabled and the `gcloud` CLI installed. Check the current free-tier limits and sign-up credits before the session, and use a budget alert.

```bash
gcloud auth login
gcloud config set project <PROJECT_ID>
cd lab/visit-counter
gcloud run deploy cloudtrack-<your-name> \
  --source . \
  --region <nearest-region> \
  --allow-unauthenticated
```
The command builds your Dockerfile and prints a URL. Open it and `curl` `/health`.

Notes:
- Cloud Run injects `PORT`, which is why our app reads it.
- Cloud Run has no Redis here, so the app uses the in-memory counter. Refresh a few times, then wait for the service to scale to zero and refresh again. This shows why managed state stores exist.

### Clean up (important)
```bash
gcloud run services delete cloudtrack-<your-name> --region <nearest-region>
```

## Option B: Push to a registry (no cloud billing needed)

```bash
echo <TOKEN> | docker login ghcr.io -u <github-username> --password-stdin
docker tag visit-counter ghcr.io/<github-username>/visit-counter:0.1
docker push ghcr.io/<github-username>/visit-counter:0.1
```
Use a token with `write:packages`. Then anyone can `docker run` your image from the registry.

## Reflection
1. What changed between "runs on my laptop" and "runs in the cloud"?
2. Which parts of the app are stateless, and which are not?
3. What would you add before calling this production-ready?
