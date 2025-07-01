import os
import redis

from typing import Optional
from dotenv import load_dotenv


load_dotenv()


class RedisConfig:
    def __init__(self):
        # Set Redis client configuration
        self.host = os.getenv('REDIS_CLOUD_CLIENT_HOST')
        self.port = int(os.getenv('REDIS_CLOUD_CLIENT_PORT'))
        self.username = os.getenv('REDIS_CLOUD_CLIENT_USERNAME')
        self.password = os.getenv('REDIS_CLOUD_CLIENT_PASSWORD')

        if not self.host:
            raise ValueError("REDIS_HOST is not set")
        
        if not self.port:
            raise ValueError("REDIS_PORT is not set")
        
        if not self.username:
            raise ValueError("REDIS_USERNAME is not set")
        
        if not self.password:
            raise ValueError("REDIS_PASSWORD is not set")
        
        # Set connection pool configuration
        self.socket_connect_timeout = int(os.getenv('REDIS_SOCKET_CONNECT_TIMEOUT', '5'))
        self.socket_timeout = int(os.getenv('REDIS_SOCKET_TIMEOUT', '5'))
        self.retry_on_timeout = os.getenv('REDIS_RETRY_ON_TIMEOUT', 'True').lower() == 'true'
        self.health_check_interval = int(os.getenv('REDIS_HEALTH_CHECK_INTERVAL', '30'))
        
    def get_connection_kwargs(self) -> dict:
        """Get Redis connection parameters as a dictionary."""
        return {
            'host': self.host,
            'port': self.port,
            'username': self.username,
            'password': self.password,
            'socket_connect_timeout': self.socket_connect_timeout,
            'socket_timeout': self.socket_timeout,
            'retry_on_timeout': self.retry_on_timeout,
            'health_check_interval': self.health_check_interval,
        }


# Set Redis configuration
config = RedisConfig()

# Set Redis connection pool
_connection_pool: Optional[redis.ConnectionPool] = None


def get_connection_pool() -> redis.ConnectionPool:
    """Get or create Redis connection pool."""
    global _connection_pool
    if _connection_pool is None:
        _connection_pool = redis.ConnectionPool(**config.get_connection_kwargs())
    return _connection_pool


def get_redis_connection() -> redis.Redis:
    """Get a Redis connection from the pool."""
    return redis.Redis(connection_pool=get_connection_pool())


def check_redis_connection() -> bool:
    """Test Redis connection."""
    try:
        client = get_redis_connection()
        client.ping()
        return True
    except Exception as e:
        print(f"Redis connection failed: {e}")
        return False


# Set global Redis client instance
redis_client = get_redis_connection()


def get_rq_connection() -> redis.Redis:
    """Get Redis connection for RQ workers."""
    return get_redis_connection() 