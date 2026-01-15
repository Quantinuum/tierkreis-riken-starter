from pathlib import Path
from sys import argv
import time
from typing import Any
from pytket.qasm.qasm import circuit_from_qasm
from tierkreis.graphs.simulate.compile_simulate import compile_simulate
from uuid import UUID

from tierkreis.controller import run_graph  # type: ignore
from tierkreis.storage import FileStorage, read_outputs  # type: ignore
from tierkreis.executor import UvExecutor, TaskExecutor, PJSUBExecutor
from tierkreis.controller.executor.hpc.job_spec import JobSpec, ResourceSpec

from workflows.consts import WORKERS_DIR

simulator_name = "aer"
circuit = circuit_from_qasm(Path(__file__).parent / "data" / "ghz_state_n23.qasm")
circuits = [circuit] * 3


if __name__ == "__main__":
    try:
        group_name = argv[1]
    except IndexError:
        raise ValueError("Please provide your group_id as the first argument.")

    g = compile_simulate()

    storage = FileStorage(UUID(int=107), do_cleanup=True)
    logs_path = storage.logs_path

    uv = UvExecutor(WORKERS_DIR, logs_path)
    spec = JobSpec(
        job_name="tkr_symbolic_ciruits",
        account=group_name,
        command="env UV_PROJECT_ENVIRONMENT=compute_venv uv run main.py",
        resource=ResourceSpec(nodes=1, memory_gb=None, gpus_per_node=None),
        walltime="00:15:00",
        output_path=Path(logs_path),
        error_path=Path(logs_path),
        include_no_check_directory_flag=True,
    )
    pjsub = PJSUBExecutor(spec=spec, registry_path=WORKERS_DIR, logs_path=logs_path)
    executor = TaskExecutor(
        {"qulacs_worker.run_circuit": pjsub, "aer_worker.run_circuit": pjsub, "*": uv},
        storage,
    )

    inputs: dict[str, Any] = {
        "circuits": circuits,
        "n_shots": [3] * len(circuits),
        "simulator_name": simulator_name,
        "compilation_optimisation_level": 2,
    }
    inputs["simulator_name"] = "qulacs"

    print("Simulating using qulacs...")
    storage.clean_graph_files()
    start = time.time()
    run_graph(storage, executor, g, inputs, polling_interval_seconds=0.1)
    print(f"time taken: {time.time() - start}")
    res = read_outputs(g, storage)
    assert isinstance(res, list)
    print(len(res))
