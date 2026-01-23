OPENQASM 3.0;
include "stdgates.inc";
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
bit[2] c;
qubit[68] node;
rz(pi/2) node[66];
rz(7*pi/2) node[67];
sx node[66];
sx node[67];
rz(pi) node[66];
rzz(pi/2) node[66], node[67];
c[0] = measure node[66];
rz(pi/2) node[67];
sx node[67];
c[1] = measure node[67];