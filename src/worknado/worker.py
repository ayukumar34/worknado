from worknado.config.redis_config import check_redis_connection


def main():
    """Simple worker that checks Redis connection."""
    if check_redis_connection():
        print("Successfully connected to Redis!")
    else:
        print("Failed to connect to Redis.")


if __name__ == "__main__":
    main()