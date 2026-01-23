from pathlib import Path
from sys import argv
from tierkreis.pkg import install_dependencies, remove_dependencies, clear_cache
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
    ),
    "aer_worker": GitHubDependency(
        account="quantinuum",
        repo="tierkreis",
        subdirectory="tierkreis_workers/aer_worker",
        branch="chore/tierkreis-riken-starter",
    ),
}

if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == "--remove":
        remove_dependencies(list(deps.keys()), Path.cwd() / "workers_external")
    elif len(argv) > 1 and argv[1] == "--clean":
        remove_dependencies(list(deps.keys()), Path.cwd() / "workers_external")
        clear_cache()
    else:
        install_dependencies(deps, Path.cwd() / "workers_external")
