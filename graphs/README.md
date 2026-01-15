# Example graphs

## Executors used

- [UvExecutor](https://quantinuum.github.io/tierkreis/apidocs/tierkreis/tierkreis.controller.executor.uv_executor.html#tierkreis.controller.executor.uv_executor.UvExecutor) is used to run tasks in Python workers. These tasks will run on the Fugaku login node.
- [PJSUBExecutor](https://quantinuum.github.io/tierkreis/executors/hpc/pjsub-fugaku.html) is an [HPC executor](https://quantinuum.github.io/tierkreis/executors/hpc.html) used to run tasks on the Fugaku compute nodes with `pjsub`.
- `TaskExecutor` routes tasks to different executors based on the tasks's fully qualified name. Glob expressions are used to route multiple tasks to a single executor.

## compile_run_ibm.py

- Uses the Riken quantum C API to get the current transpilation information for IBM Kobe.
- Compiles a simple circuit using `pytket` using the transpilation information.
- Submits the compiled circuit to IBM Kobe for execution.
- Parses the output of IBM Kobe giving results as a dictionary where the keys are classical register names and the values are lists of shots.

## compile_run_reimei.py

- Compiles the inputs circuit for use on Quantinuum Reimei.
- Submits the compiled circuit to Quantinuum Reimei for execution.
- Parses the output giving results as a dictionary where the keys are classical register names and the values are lists of shots.

## compile_run_reimei_simulator.py

- Compiles the inputs circuit for use on Quantinuum Reimei.
- Submits the compiled circuit to the Quantinuum Reimei simulator for execution.
- Parses the output giving results as a dictionary where the keys are classical register names and the values are lists of shots.
