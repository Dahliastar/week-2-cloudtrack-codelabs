import os

from flask import Flask

app = Flask(__name__)

# If REDIS_URL is set we count in Redis (persists). Otherwise we count in memory (resets).
redis_client = None
if os.getenv("REDIS_URL"):
    import redis

    redis_client = redis.Redis.from_url(os.environ["REDIS_URL"])

memory_hits = 0


@app.get("/")
def index():
    global memory_hits
    if redis_client:
        count = redis_client.incr("hits")
    else:
        memory_hits += 1
        count = memory_hits
    return f"Hello from Cloud Track! Visits: {count}\n"


@app.get("/health")
def health():
    return "ok\n"
