from nautobot.extras.jobs import Job

class MemoryIntensiveJob(Job):
    description = "Job that allocates approximately 2GB of memory for testing purposes."

    def run(self, data, commit):
        # Allocate a list with 2^28 elements, each being a 1-byte string
        large_list = ['a'] * (2**28)
        self.log_info("Allocated approximately 2GB of memory.")
        # Perform any additional operations as needed
