set -euo pipefail

DIR=$(dirname $0)

echo "Auth reimei-simulator"
. /vol0300/share/ra010014/jhpcq/x86/scripts/install-cert-files.sh reimei-simulator;
source /vol0003/share/ra010014/jhpcq/bin/jhpc-q-setup.sh
fetch_qtm_jwt.py
cp $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt-reimei-simulator.token
mv $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt.token

echo "Run reimei-simulator"
. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh reimei-simulator
sqcsub --nqubits 10 \
    --nshots 30 \
    --ifile ${DIR}/simple_reimei_simulator.qasm \
    --iformat qasm \
    --ofile ${DIR}/result.txt \
    --oformat raw \
    --qpu reimei-simulator


echo "Auth IBM Kobe"
. /vol0300/share/ra010014/jhpcq/x86/scripts/install-cert-files.sh ibm-kobe-dacc;
source /vol0003/share/ra010014/jhpcq/bin/jhpc-q-setup.sh
fetch_qtm_jwt.py
cp $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt-ibm-kobe-dacc.token
# mv $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt.token

echo "Run reimei-simulator"
. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh reimei-simulator
sqcsub --nqubits 10 \
    --nshots 30 \
    --ifile ${DIR}/simple_reimei_simulator.qasm \
    --iformat qasm \
    --ofile ${DIR}/result.txt \
    --oformat raw \
    --qpu reimei-simulator