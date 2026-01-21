from pathlib import Path

CUSTOM_WORKERS_REGISTRY = Path(__file__).parent.parent / "workers"
EXTERNAL_WORKERS_REGISTRY = Path(__file__).parent.parent / "workers_external"
REGISTRIES = [CUSTOM_WORKERS_REGISTRY, EXTERNAL_WORKERS_REGISTRY]
TKR_DIR = Path.home() / ".tierkreis"
