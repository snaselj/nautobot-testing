import time

from nautobot.apps.jobs import IntegerVar, Job


def consume_memory(size_in_mb):
    block = bytearray(size_in_mb * 1024 * 1024)
    return block


class MemoryIntensiveJob(Job):
    request_memory_megabytes = IntegerVar(default=1024)
    steps_count = IntegerVar(default=2)
    step_delay_seconds = IntegerVar(default=60)

    class Meta:  # type: ignore
        description = "Job consuming memory in steps for testing"

    def run(self, request_memory_megabytes, steps_count, step_delay_seconds):
        mem_blocks = []
        mb_per_step = request_memory_megabytes // steps_count

        for step in range(steps_count):
            self.logger.info(f"Step {step + 1}/{steps_count}, consuming {mb_per_step * step + 1}/{request_memory_megabytes} MB of memory")
            mem_blocks.append(consume_memory(mb_per_step))
            time.sleep(step_delay_seconds)

        self.logger.info("Job completed successfully")
