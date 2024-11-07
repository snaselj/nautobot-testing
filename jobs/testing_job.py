import time

from nautobot.apps.jobs import IntegerVar, Job


def consume_memory(size_in_mb):
    block = bytearray(size_in_mb * 1024 * 1024)
    return block


class MemoryIntensiveJob(Job):
    request_memory = IntegerVar(default=1024)
    number_of_steps = IntegerVar(default=2)
    delay = IntegerVar(default=60)

    class Meta:  # type: ignore
        description = "Job that allocates approximately 2GB of memory for testing purposes."

    def run(self, request_memory, number_of_steps, delay):
        mem_blocks = []
        mb_per_step = request_memory // number_of_steps

        for step in range(number_of_steps):
            self.logger.info(f"Step {step + 1}/{number_of_steps}")
            mem_blocks.append(consume_memory(mb_per_step))
            time.sleep(delay)

        print("Job completed successfully.")
        return f"Job completed successfully after {number_of_steps} steps."
