# Example graphs

## Executors used

- [UvExecutor](https://quantinuum.github.io/tierkreis/apidocs/tierkreis/tierkreis.controller.executor.uv_executor.html#tierkreis.controller.executor.uv_executor.UvExecutor) is used to run tasks in Python workers. These tasks will run on the Fugaku login node.
- [PJSUBExecutor](https://quantinuum.github.io/tierkreis/executors/hpc/pjsub-fugaku.html) is an [HPC executor](https://quantinuum.github.io/tierkreis/executors/hpc.html) used to run tasks on the Fugaku compute nodes with `pjsub`.
  - If we want to run a Python worker using `uv` using the `PJSUBExecutor` then we should add the env var `env UV_PROJECT_ENVIRONMENT=compute_venv` to the command in the `JobSpec`. This will ensure separation of Python virtual environments between the login and compute nodes. For an example see `graphs/simulate_aer.py`.
- `TaskExecutor` routes tasks to different executors based on the task's fully qualified name. Glob expressions are used to route multiple tasks to a single executor.

## Graph descriptions

### compile_run_ibm.py

Compile and run a circuit on IBM Kobe.

- Uses the Riken quantum C API to get the current transpilation information for IBM Kobe.
- Compiles a simple circuit using `pytket` using the transpilation information.
- Submits the compiled circuit to IBM Kobe for execution.
- Parses the output of IBM Kobe giving results as a dictionary where the keys are classical register names and the values are lists of shots.

### compile_run_reimei.py

Compile and run a circuit on Quantinuum Reimei.

- Compiles the inputs circuit for use on Quantinuum Reimei.
- Submits the compiled circuit to Quantinuum Reimei for execution.
- Parses the output giving results as a dictionary where the keys are classical register names and the values are lists of shots.

### compile_run_reimei_simulator.py

Compile and run a circuit on the Quantinuum Reimei simulator.

- Compiles the inputs circuit for use on Quantinuum Reimei.
- Submits the compiled circuit to the Quantinuum Reimei simulator for execution.
- Parses the output giving results as a dictionary where the keys are classical register names and the values are lists of shots.

### simulate_aer.py

Use `pjsub` to run simulations on the Fugaku compute nodes with Qiskit Aer.

- This script takes as an argument the group name under which we submit compute node jobs to Fugaku using `pjsub`.
- Uses the `TaskExecutor` to run the `run_circuit` task of the `aer_worker` to run using `pjsub` but all other tasks on the login node. Changing the dictionary input to `TaskExecutor` will change which tasks run on the compute nodes and which tasks run on the login node.
- The graph `compile_simulate` is a graph provided by the Tierkreis library. It takes a list of circuits and compiles them for Qiskit Aer and then executes them on Qiskit Aer. Using the Tierkreis MAP node the compilation and execution of all of the circuits is done in parallel.
