# Part 3: Docker basics (live, 30 min)

**Image** = read-only template. **Container** = a disposable running copy of it. **Dockerfile** = the recipe that builds an image.

```
Dockerfile --build--> Image --run--> Container
```

Check you are ready: `docker run hello-world` should print a welcome message.

> **Instructor tip:** before running each command, ask the room what they expect to happen.

## Lab 1: Run something that already exists (7 min)

```bash
docker run -d -p 8080:80 --name web nginx
docker ps
curl localhost:8080
docker logs web
docker exec -it web sh      # try: ls, whoami, then exit
docker stop web
docker rm web
```

Questions:
1. What does `-p 8080:80` mean? (host port : container port)
2. What does `-d` do?
3. What happens if you skip `--name`?

## Lab 2: Build your own image (13 min)

We use the **Visit Counter**, a tiny Flask app in [`lab/visit-counter`](lab/visit-counter). It is the project we will keep improving in Labs 4 to 6.

```bash
cd lab/visit-counter
cat Dockerfile
docker build -t visit-counter .
docker run -d -p 8080:8080 --name counter visit-counter
curl localhost:8080
curl localhost:8080
curl localhost:8080/health
```

The count goes up on each request.

### See the build cache
1. Edit one line of `app.py` (change the greeting).
2. Run `docker build -t visit-counter .` again.
3. Watch which steps say `CACHED`. Dependencies are not reinstalled because `requirements.txt` is copied *before* the app code.

### Prove the count lives inside the container
```bash
docker restart counter && curl localhost:8080    # count continues
docker rm -f counter
docker run -d -p 8080:8080 --name counter visit-counter
curl localhost:8080                              # back to 1
```

### Break it on purpose
Change `0.0.0.0` to `127.0.0.1` in the `CMD`, rebuild and run. `curl` fails. Why? (Inside a container, `127.0.0.1` is the container itself, so the published port cannot reach the app.) Change it back.

## Lab 3: Containers are disposable (10 min)

```bash
docker run -d --name cache redis:7-alpine
docker exec -it cache redis-cli set hello world
docker exec -it cache redis-cli get hello
docker rm -f cache
docker run -d --name cache redis:7-alpine
docker exec -it cache redis-cli get hello      # (nil): the data is gone
```

Fix it with a **volume**:
```bash
docker rm -f cache
docker run -d --name cache -v redis-data:/data redis:7-alpine redis-server --save 1 1
docker exec -it cache redis-cli set hello world
docker exec -it cache redis-cli save
docker rm -f cache
docker run -d --name cache -v redis-data:/data redis:7-alpine
docker exec -it cache redis-cli get hello      # "world" survived
```

Rule of thumb: **never store anything you care about only inside a container.**

## Clean up
```bash
docker rm -f counter cache
docker rmi visit-counter
docker volume rm redis-data
docker ps -a && docker images
```
`docker system prune` removes all stopped containers and unused images. Read the prompt before you confirm.

## Common problems
| Symptom | Likely cause |
|---|---|
| `Cannot connect to the Docker daemon` | Docker Desktop or the daemon is not running |
| `permission denied` on Linux | Add your user to the `docker` group, then log out and in |
| `port is already allocated` | Something else uses 8080; change the left side of `-p` |
| Container runs but `curl` fails | App bound to `127.0.0.1`, or wrong port mapping |
| `name is already in use` | Old container exists: `docker rm -f <name>` |

## Take-home
Continue with [Lab 4: Compose](04-compose.md), [Lab 5: Harden](05-harden.md) and [Lab 6: Ship](06-ship.md).
