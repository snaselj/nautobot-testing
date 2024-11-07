from nautobot.apps.jobs import register_jobs

from .jobs.testing_job import MemoryIntensiveJob

register_jobs(MemoryIntensiveJob)
