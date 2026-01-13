from os import symlink
from pathlib import Path
import subprocess
from typing import Literal

from pydantic import BaseModel

WORKER_CACHE = Path.home() / ".tierkreis" / "workers" / "github"


class GitHubDependency(BaseModel):
    type: Literal["github"] = "github"

    account: str
    repo: str
    subdirectory: str

    branch: str = "main"

    def install(self, worker_name: str, target_dir: Path):
        cache_dir = WORKER_CACHE / self.account / self.repo
        cache_dir.mkdir(exist_ok=True, parents=True)

        git_dir = cache_dir / ".git"
        git_url = f"https://github.com/{self.account}/{self.repo}"
        if not git_dir.exists():
            subprocess.run(["git", "clone", git_url, "."], cwd=cache_dir)

        subprocess.run(["git", "checkout", self.branch], cwd=cache_dir)
        subprocess.run(["git", "pull"], cwd=cache_dir)

        worker_dir = target_dir / worker_name
        if worker_dir.exists():
            worker_dir.unlink()

        symlink(cache_dir / self.subdirectory, worker_dir, target_is_directory=True)


class PathDependency(BaseModel):
    type: Literal["path"] = "path"

    worker_dir: Path

    def install(self, worker_name: str, target_dir: Path):
        """Not implemented..."""
        return


TKRDependency = GitHubDependency | PathDependency

deps = {
    "tkr_ibm_kobe": GitHubDependency(
        account="quantinuum",
        repo="tierkreis-riken",
        subdirectory="workers/tkr_ibm_kobe",
    ),
    "tkr_ibm_kobe_pjsub": GitHubDependency(
        account="quantinuum",
        repo="tierkreis-riken",
        subdirectory="workers/tkr_ibm_kobe",
    ),
    "tkr_reimei": GitHubDependency(
        account="quantinuum",
        repo="tierkreis-riken",
        subdirectory="workers/tkr_reimei",
        branch="chore/tierkreis-riken-starter",
    ),
    "tkr_reimei_pjsub": GitHubDependency(
        account="quantinuum",
        repo="tierkreis-riken",
        subdirectory="workers/tkr_reimei",
        branch="chore/tierkreis-riken-starter",
    ),
    "nexus_worker": GitHubDependency(
        account="quantinuum",
        repo="tierkreis",
        subdirectory="tierkreis_workers/nexus_worker",
    ),
}


def install_workers(deps: dict[str, GitHubDependency], target_dir: Path):
    for worker_name, dep in deps.items():
        dep.install(worker_name, target_dir)


if __name__ == "__main__":
    install_workers(deps=deps, target_dir=Path.cwd() / "workers")
