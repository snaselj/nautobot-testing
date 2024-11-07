from nautobot.extras.models import GitRepository

repository_name = "snaselj/nautobot-testing"
repository, created = GitRepository.objects.update_or_create(
    name=repository_name,
    defaults={
        "remote_url": f"https://github.com/{repository_name}.git",
        "branch": "main",
        "provided_contents": ["jobs"],
    },
)

if created:
    print(f"Git repository '{repository_name}' created and set to fetch Jobs.")
else:
    print(f"Git repository '{repository_name}' updated.")

repository.sync()
