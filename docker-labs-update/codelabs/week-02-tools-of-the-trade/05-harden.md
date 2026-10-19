# Lab 5: Harden the image (self-paced, 20 min)

Working is not the same as safe. Make three improvements to the Visit Counter image.

## 1. Stop running as root
```bash
docker build -t visit-counter .
docker run -d --name counter -p 8080:8080 visit-counter
docker exec counter whoami          # root
docker rm -f counter
```
Add to the Dockerfile before `ENV PORT=8080`:
```dockerfile
RUN useradd --create-home appuser
USER appuser
```
Rebuild, run and confirm `whoami` prints `appuser`.

## 2. Add a healthcheck
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import os,urllib.request; urllib.request.urlopen('http://localhost:'+os.environ.get('PORT','8080')+'/health')"
```
Run it, wait about 30 seconds, then `docker ps` and look for `(healthy)`.

## 3. Check size and vulnerabilities
```bash
docker images | grep -E "visit-counter|python"
docker pull python:3.12
docker images python
```
Compare `python:3.12` with `python:3.12-slim`.

Scan the image with whichever is available:
```bash
docker scout quickview visit-counter
# or
trivy image visit-counter
```
Read the summary. You are not expected to fix everything; learn to read the output.

## Rules of thumb
- Run as non-root
- Use slim or minimal base images and pin versions
- Never put secrets in the image or in `ENV`
- Keep a `.dockerignore`

A finished version is in [`Dockerfile.hardened`](lab/visit-counter/Dockerfile.hardened). Try before you peek.

## Check yourself
1. Why does a non-root user matter if the container is already isolated?
2. Why pin dependency versions?
