DIR=$(dirname $0)

source ${DIR}/auth_reimei.sh

. /vol0300/share/ra010014/jhpcq/x86/scripts/setenv-sqcsub.sh reimei
sqcsub --nqubits 10 \
    --nshots 30 \
    --ifile ${DIR}/simple_reimei.qasm \
    --iformat qasm \
    --ofile ${DIR}/result.txt \
    --oformat raw \
    --qpu reimei
