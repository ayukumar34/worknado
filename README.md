## Worknado

A Python project designed to bootstrap Redis Queue-based asynchronous workers using Redis Cloud. It provides a minimal yet scalable setup for building distributed task queues, with extensibility in mind for additional features.

### ✨ Features

- 🔧 Minimal Redis Cloud Client Configuration
- 🎯 Simple Redis Queue Worker with Job Queueing
- 📦 Poetry-based dependency management
- 🛠️ Easily extendable for production use cases

### 🚀 Installation

1. Install [Poetry](https://python-poetry.org/docs/)

2. Clone the repository:
   ```bash
   git clone https://github.com/ayukumar34/worknado.git
   cd worknado

3. Install dependencies:
   ```bash
   poetry lock
   poetry install

4. Add the following environment variables to `.env`:
   ```bash
   REDIS_CLOUD_CLIENT_HOST="redis-XXXXX.XXXX.us-east-1-4.ec2.redns.redis-cloud.com"
   REDIS_CLOUD_CLIENT_PORT="XXXXX"
   REDIS_CLOUD_CLIENT_USERNAME="default"
   REDIS_CLOUD_CLIENT_PASSWORD="********************"

5. Run the Redis Queue worker:
   ```bash
   poetry run python src/worknado/worker.py

6. Enqueue a job payload:
   ```python
    from rq import Queue
    from worknado.config.redis_config import redis_client
    
    queue = Queue("default", connection=redis_client)
    
    def say_hello(name: str):
        return f"Hello, {name}!"
    
    # Enqueue job
    job = queue.enqueue(simple_job, "Ayush")

### 📄 License

MIT License. Use this boilerplate freely for personal and commercial projects.
