from tierkreis import Worker
from pytket import Circuit  # type: ignore


worker = Worker("example_worker")


@worker.task()
def circ1():
    circ = Circuit(4)
    circ.X(0)
    circ.CX(1, 3)
    circ.Z(3)
    circ.measure_all()
    return circ


@worker.task()
def circ2():
    circ = Circuit(2)
    circ.H(0)
    circ.CX(0, 1)
    circ.measure_all()
    return circ


@worker.task()
def deterministic() -> Circuit:
    circ = Circuit(2, 2)
    circ.X(1).measure_all()
    return circ
