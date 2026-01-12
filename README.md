# tierkreis-riken-starter

Example projects and workflows for using Tierkreis on Riken (Fugaku)

## Set up

Clone this repo to the Fugaku login node.

### Registration smoke tests

In order to access Quantinuum Reimei or IBM Kobe an out-of-band registration process is required.
The registration process is out of scope for this repository but the following scripts can be used to veryify that this part has been set up correctly.
From the root of the repository run the following commands, which will prompt for the credentials used to access Quantinuum Reimei and/or IBM Kobe.

```bash
./tests/smoke_tests/test_reimei_simulator.sh
```

```bash
./tests/smoke_tests/test_ibm_kobe.sh
```

If there are errors at this point then the registration process is not completed or there is an error with a device.

### Install uv

We install `uv` twice: once for the login node and once for the compute nodes.

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

Confirm that the correct `uv` is selected for the login node:

```bash
$ which uv
~/.local/bin_x86_64/uv
```

When using `uv` on the compute nodes, we will directly use `~/.local/bin_aarch64/uv`.

### Install workers

```bash
uv run ./install_workers/py
```

### Post install step for IBM Kobe

```bash
cd workers/ibm_kobe
./scripts/build.sh
```
