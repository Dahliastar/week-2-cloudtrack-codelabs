# Part 3: Docker basics

**Image** = the recipe (read-only template). **Container** = a running instance of it. **Dockerfile** = the instructions that build an image.

## Checkpoint 0: first container
```bash
docker run hello-world
docker ps -a
docker images
```

## Checkpoint 1: look at the lab app
Open [`lab/hello-web/`](lab/hello-web). It has a tiny Python web server and a Dockerfile.

## Checkpoint 2: build and run
```bash
cd lab/hello-web
docker build -t hello-web .
docker run -d -p 8000:8000 --name web hello-web
curl localhost:8000
```
`-d` runs in the background. `-p host:container` maps a port.

## Checkpoint 3: inspect
```bash
docker ps
docker logs web
docker exec -it web sh
# inside: ls, whoami, then exit
```

## Checkpoint 4: clean up
```bash
docker stop web
docker rm web
docker rmi hello-web
```
Bonus: `docker system prune` removes all stopped containers and unused images. Read the prompt before you confirm.

## Common problems
| Symptom | Likely cause |
|---|---|
| `Cannot connect to the Docker daemon` | Docker Desktop/daemon is not running |
| `permission denied` on Linux | Add your user to the `docker` group, then log out and in |
| `port is already allocated` | Something else uses 8000; change the left side of `-p` |
| Container runs but `curl` hangs or fails | App is bound to `127.0.0.1`; it must bind `0.0.0.0` |

## Think about it
1. Why does the app need to listen on `0.0.0.0` inside a container?
2. What happens to data written inside a container when you `docker rm` it?
