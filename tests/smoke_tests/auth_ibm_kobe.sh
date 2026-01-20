. /vol0300/share/ra010014/jhpcq/x86/scripts/install-cert-files.sh ibm-kobe-dacc;
source /vol0003/share/ra010014/jhpcq/bin/jhpc-q-setup.sh
fetch_qtm_jwt.py
cp $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt-ibm-kobe-dacc.token
mv $HOME/.qtm.jwt $HOME/.sqc_rpc_sched/jwt.token