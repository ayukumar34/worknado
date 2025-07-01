import time


def simple_job(name, duration=5):
    """A simple job that simulates work."""
    print(f"Hello {name}!")
    time.sleep(duration)
    print(f"Goodbye {name}!")
    return f"Job completed for {name}" 