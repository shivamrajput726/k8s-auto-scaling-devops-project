import multiprocessing
import os


bind = "0.0.0.0:8000"
workers = int(os.getenv("WEB_CONCURRENCY", str((multiprocessing.cpu_count() * 2) + 1)))
worker_class = "uvicorn.workers.UvicornWorker"
graceful_timeout = 30
timeout = 60
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOG_LEVEL", "info").lower()
worker_tmp_dir = "/dev/shm"
