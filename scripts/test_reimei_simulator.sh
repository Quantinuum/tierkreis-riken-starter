DIR=$(dirname $0)

source ${DIR}/auth_reimei_simulator.sh

. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh reimei-simulator
sqcsub --nqubits 10 \
    --nshots 30 \
    --ifile ${DIR}/simple_reimei_simulator.qasm \
    --iformat qasm \
    --ofile ${DIR}/result.txt \
    --oformat raw \
    --qpu reimei-simulator
