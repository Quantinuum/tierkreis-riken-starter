DIR=$(dirname $0)

. /vol0300/share/ra010014/jhpcq/x86/scripts/install-cert-files.sh reimei;
source /vol0003/share/ra010014/jhpcq/bin/jhpc-q-setup.sh
fetch_qtm_jwt.py
mv $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt.token

. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh reimei-simulator
sqcsub --nqubits 10 --nshots 30 --ifile /home/u13620/_scr/41e0a199-96ea-4867-8a60-0c810e596f5c/circ.in --iformat qasm --ofile ${DIR}/result.txt --oformat raw --qpu reimei-simulator
