import os
from dotenv import load_dotenv


load_dotenv()


class Settings:    
    # Environment variables
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # Redis Queue Configuration
    RQ_DEFAULT_QUEUE = os.getenv('RQ_DEFAULT_QUEUE', 'default')
    RQ_HIGH_QUEUE = os.getenv('RQ_HIGH_QUEUE', 'high')
    RQ_LOW_QUEUE = os.getenv('RQ_LOW_QUEUE', 'low')
    
    # Worker Configuration
    WORKER_TIMEOUT = int(os.getenv('WORKER_TIMEOUT', '180'))
    WORKER_RESULT_TTL = int(os.getenv('WORKER_RESULT_TTL', '500'))
    WORKER_FAILURE_TTL = int(os.getenv('WORKER_FAILURE_TTL', '86400'))
    
    # Job Configuration
    JOB_TIMEOUT = int(os.getenv('JOB_TIMEOUT', '3600'))
    JOB_RESULT_TTL = int(os.getenv('JOB_RESULT_TTL', '86400'))
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production environment."""
        return cls.ENVIRONMENT.lower() == 'production'
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development environment."""
        return cls.ENVIRONMENT.lower() == 'development'


# Global settings instance
settings = Settings() 