# Graphs for running computations on Fugaku

## Executors used

- [UvExecutor](https://quantinuum.github.io/tierkreis/apidocs/tierkreis/tierkreis.controller.executor.uv_executor.html#tierkreis.controller.executor.uv_executor.UvExecutor) is used to run tasks in Python workers. These tasks will run on the Fugaku login node.
- [PJSUBExecutor](https://quantinuum.github.io/tierkreis/executors/hpc/pjsub-fugaku.html) is an [HPC executor](https://quantinuum.github.io/tierkreis/executors/hpc.html) used to run tasks on the Fugaku compute nodes with `pjsub`.
- `TaskExecutor` routes tasks to different executors based on the tasks's fully qualified name. Glob expressions are used to route multiple tasks to a single executor.

## compile_run_ibm.py
