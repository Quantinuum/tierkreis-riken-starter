from pathlib import Path
from tierkreis.pkg import install_dependencies
from tierkreis.pkg.base import TKRDependency
from tierkreis.pkg.github import GitHubDependency

deps: dict[str, TKRDependency] = {
    "tkr_ibm_kobe": GitHubDependency(
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
    "nexus_worker": GitHubDependency(
        account="quantinuum",
        repo="tierkreis",
        subdirectory="tierkreis_workers/nexus_worker",
    ),
}

if __name__ == "__main__":
    install_dependencies(deps=deps, target_dir=Path.cwd() / "workers")
