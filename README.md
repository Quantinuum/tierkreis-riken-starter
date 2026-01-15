# Tierkreis Riken starter project

Example project for using Tierkreis on Fugaku (Riken).

## Project structure

- `graphs`: The Tierkreis graphs that specify the order of execution of our computations.
- `workers`: Each subdirectory constitutes a worker. A worker is a collection of task definitions that have a common set of dependencies.
- `install_workers.py`: An example script to demonstrate how to pull in dependencies used in the graphs in `graphs`.
- `pyproject.toml`: The dependencies required to run the graphs in `graphs`. Worker dependencies should not be included.

## Set up

Clone this repo to the Fugaku login node.

### Registration smoke tests

In order to access Quantinuum Reimei or IBM Kobe an out-of-band registration process is required.
The registration process is out of scope for this README but the following scripts can be used to verify that this part has been set up correctly.
From the root of the repository run the following commands, which will prompt for the credentials used to access Quantinuum Reimei and/or IBM Kobe.

```bash
./tests/smoke_tests/test_reimei_simulator.sh
```

```bash
./tests/smoke_tests/test_ibm_kobe.sh
```

If there are errors at this point then the registration process is not completed or there is an error with a device.

### Device switching

Currently one must manually switch between QPUs with the following commands before using the Tierkreis worker corresponding to the QPU:

```bash
. /vol0300/share/ra010014/jhpcq/x86/scripts/install-cert-files.sh <QPU_NAME>;
source /vol0003/share/ra010014/jhpcq/bin/jhpc-q-setup.sh
fetch_qtm_jwt.py
mv $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt.token
```

where `<QPU_NAME>` is one of `ibm-kobe-dacc`, `reimei` or `reimei-simulator`.

### Install uv

We install `uv` twice because of the difference in architecture between the login and compute nodes.

For the login node:

```bash
wget https://github.com/astral-sh/uv/releases/download/0.9.24/uv-x86_64-unknown-linux-gnu.tar.gz -P /tmp/uv
tar -C $HOME/.local/bin_x86_64/ -xvzf /tmp/uv/uv-x86_64-unknown-linux-gnu.tar.gz --strip-components=1
```

For the compute node

```bash
wget https://github.com/astral-sh/uv/releases/download/0.9.24/uv-aarch64-unknown-linux-gnu.tar.gz -P /tmp/uv
tar -C $HOME/.local/bin_aarch64/ -xvzf /tmp/uv/uv-aarch64-unknown-linux-gnu.tar.gz --strip-components=1
```

Then add the following to `.bashrc` to select the correct one:

```bash
. "$HOME/.local/bin_$(uname -p)/env"
```

Confirm that the correct `uv` is selected for the login node, after starting a new session

```bash
$ which uv
~/.local/bin_x86_64/uv
```

### Install workers

Custom workers can be created as new folders in the `./workers` directory.
An example of how to install some workers from GitHub is given by the file `install_workers.py`.
So running

```bash
uv run ./install_workers.py
```

will pull in some remote Python workers from GitHub.
You can change the `deps` variable to pull in different workers.

### Manual worker preparations (optional)

One can make manual preparations for the workers by using an interactive environment.

```bash
pjsub --interact -g <GROUP_NAME> -L "node=1" -L "elapse=20:00" --sparam "wait-time=600" --no-check-directory
```

and then `cd` into each worker directory and make any manual preparations you require.
E.g.

```bash
cd workers/aer_worker
env UV_PROJECT_ENVIRONMENT=compute_venv uv sync
```

will save time by installing the dependencies before running your workflow.
This is strictly speaking not necessary because `uv` will always perform a sync when running `uv run`.

### Post install step for IBM Kobe

The worker for interacting with IBM Kobe needs a special post-install step,
which builds C code for interacting directly with the Riken C API for QPUs.
The script that performs the post-install operations is very specific to Fugaku and so will error if run elsewhere.

```bash
cd workers/tkr_ibm_kobe
./scripts/build.sh
```

## Running Tierkreis graphs

Each graph in the `graphs` directory can be executed with `uv`.
E.g.

```bash
uv run graphs/compile_run_reimei_simulator.py
```

see the [README](./graphs/README.md) in the `graphs` directory for individual descriptions.
