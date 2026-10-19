# Lab 4: Multi-container with Compose (self-paced, 15 min)

Typing long `docker run` commands for two containers gets old. Compose describes the whole stack in one file.

## Run it
```bash
cd lab/visit-counter
cat compose.yaml
docker compose up --build -d
curl localhost:8080
curl localhost:8080
docker compose ps
docker compose logs web
```

The count now lives in Redis, so it survives restarts of the web container.

## Experiments
1. `docker compose restart web`, then `curl` again. Count continues.
2. `docker compose down`, then `up -d` again. Count continues, because the named volume survived.
3. `docker compose down -v`, then `up -d`. Count resets, because `-v` removed the volume.

## Understand it
- Services find each other by **service name**: `REDIS_URL` uses `redis`, not `localhost`.
- Configuration comes from **environment variables**. The same image ran without Redis in Lab 2.

## Break it on purpose
Change `redis://redis:6379` to `redis://localhost:6379` and run `docker compose up -d`. Check `docker compose logs web`. Why does it fail?

## Clean up
```bash
docker compose down -v
```

## Check yourself
1. Which line gives Redis persistence?
2. What is the difference between `down` and `down -v`?
