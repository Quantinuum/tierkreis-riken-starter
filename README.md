# tierkreis-riken-starter

Example projects and workflows for using Tierkreis on Riken (Fugaku)

## Set up

Clone this repo to the Fugaku login node.

### Registration smoke tests

In order to access Quantinuum Reimei or IBM Kobe an out-of-band registration process is required.
The registration process is out of scope for this repository but the following scripts can be used to veryify that this part has been set up correctly.
From the root of the repository run the following commands, which will prompt for the credentials used to access Quantinuum Reimei and/or IBM Kobe.

```bash
./smoke_tests/test_reimei_simulator.sh
```

```bash
./smoke_tests/test_ibm_kobe.sh
```

### Install uv

### Install workers

### Post install step for IBM Kobe
