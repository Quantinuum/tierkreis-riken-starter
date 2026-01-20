DIR=$(dirname $0)

source ${DIR}/auth_ibm_kobe_dacc.sh

. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh ibm-kobe-dacc;
sqcsub --nqubits 10 \
    --nshots 30 \
    --ifile ${DIR}/simple_ibm_kobe.qasm \
    --iformat qasm \
    --ofile ${DIR}/result.txt \
    --oformat raw \
    --qpu ibm-kobe-dacc
