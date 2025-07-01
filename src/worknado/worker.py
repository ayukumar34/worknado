from rq import Worker, Queue

from worknado.config.redis_config import check_redis_connection, get_rq_connection
from worknado.jobs import simple_job


def create_worker():
    """Create and return an RQ worker."""
    redis_conn = get_rq_connection()
    queue = Queue('default', connection=redis_conn)
    worker = Worker([queue], connection=redis_conn)
    return worker


def main():
    """Simple worker that checks Redis connection and starts RQ worker."""
    print("Starting Worknado Worker...")
    
    # Check Redis connection first
    if not check_redis_connection():
        print("Failed to connect to Redis. Exiting...")
        return
    
    print("Successfully connected to Redis!")
    
    # Create and start the worker
    try:
        worker = create_worker()
        print("RQ Worker created successfully!")
        
        # Enqueue some hardcoded simple jobs
        redis_conn = get_rq_connection()
        queue = Queue('default', connection=redis_conn)
        
        print("Enqueueing hardcoded jobs...")
        job1 = queue.enqueue(simple_job, "Archer", 3)
        print(f"Enqueued job 1: {job1.id}")
        
        job2 = queue.enqueue(simple_job, "Cyril", 2)
        print(f"Enqueued job 2: {job2.id}")
        
        job3 = queue.enqueue(simple_job, "Lana", 4)
        print(f"Enqueued job 3: {job3.id}")
        
        print(f"Total jobs in queue: {len(queue)}")
        print("Starting worker to process jobs...")
        
        worker.work()
    except KeyboardInterrupt:
        print("\nWorker stopped by user.")
    except Exception as e:
        print(f"Worker error: {e}")


if __name__ == "__main__":
    main()