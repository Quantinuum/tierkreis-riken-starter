from pathlib import Path
from uuid import UUID
from tierkreis import run_graph  # type: ignore
from tierkreis.builder import GraphBuilder
from tierkreis.controller.data.models import TKR, OpaqueType
from tierkreis.executor import UvExecutor
from tierkreis.storage import FileStorage, read_outputs  # type: ignore
from pytket.qasm.qasm import circuit_from_qasm

from workers_external.tkr_ibm_kobe.stubs import (
    get_transpile_info,
    compile_using_info,
    submit,
)
from graphs.consts import REGISTRIES

Circuit = OpaqueType["pytket._tket.circuit.Circuit"]
BackendResult = OpaqueType["pytket.backends.backendresult.BackendResult"]
g = GraphBuilder(TKR[Circuit], TKR[dict[str, list[str]]])
info = g.task(get_transpile_info())
compiled_circuit = g.task(compile_using_info(info.config, info.props, g.inputs))
res = g.task(submit(compiled_circuit, g.const(10)))
g.outputs(res)

if __name__ == "__main__":
    circuit = circuit_from_qasm(Path(__file__).parent / "data" / "ibm_question.qasm")

    storage = FileStorage(UUID(int=400), do_cleanup=True)
    exec = UvExecutor(REGISTRIES, storage.logs_path)
    run_graph(storage, exec, g, circuit, polling_interval_seconds=1)
    output = read_outputs(g, storage)
    print(output)
