from nautobot.apps.jobs import register_jobs
from .testing_job import MemoryIntensiveJob  # Import your job class

# Register the job
register_jobs(MemoryIntensiveJob)

