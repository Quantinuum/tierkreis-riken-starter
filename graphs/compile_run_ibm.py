from pathlib import Path
from uuid import UUID

from pytket.qasm.qasm import circuit_from_qasm
from tierkreis import run_graph  # type: ignore
from tierkreis.builder import GraphBuilder
from tierkreis.controller.data.models import TKR, OpaqueType
from tierkreis.executor import UvExecutor
from tierkreis.storage import FileStorage, read_outputs  # type: ignore

from graphs.consts import REGISTRIES
from workers_external.tkr_ibm_kobe.stubs import (
    compile_using_info,
    get_transpile_info,
    submit,
)

Circuit = OpaqueType["pytket._tket.circuit.Circuit"]
BackendResult = OpaqueType["pytket.backends.backendresult.BackendResult"]
g = GraphBuilder(TKR[Circuit], TKR[dict[str, list[str]]])
info = g.task(get_transpile_info())
compiled_circuit = g.task(compile_using_info(info.config, info.props, g.inputs))
res = g.task(submit(compiled_circuit, g.const(10)))
g.outputs(res)

if __name__ == "__main__":
    circuit = circuit_from_qasm(Path(__file__).parent / "data" / "simple.qasm")

    storage = FileStorage(UUID(int=400), do_cleanup=True)
    exec = UvExecutor(REGISTRIES, storage.logs_path)
    print(f"Running graph with ID {storage.workflow_id}...")
    print(f"Graph logs at ~/.tierkreis/checkpoints/{storage.workflow_id}/logs")
    run_graph(storage, exec, g, circuit, polling_interval_seconds=1)
    output = read_outputs(g, storage)
    print(output)
