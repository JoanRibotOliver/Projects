#!/bin/bash

# Renombra los ficheros pdb para incluir la fórmula

###for fich in data/pdb/*.pdb
###do
###
###  formula=$(awk '/ATOM/ {print $3}' ${fich} data/pdb/ammonia.pdb |sort | uniq -c | awk '{print $2,$1}' | tr -d ' \n')
###
###  echo mv ${fich} ${fich//.pdb/}_${formula}.pdb
###
###done

#!/bin/bash
#
# Script to rename pdb files. It inserts the formula in the filename
#
# Author: Jesus Fernandez
# Date: 2025-10-14


function get_formula(){
  fname=$1
  awk '/ATOM/ {print $3}' ${fname} | sort | uniq -c | awk '{print $2 $1}' | tr -d ' \n'
}

for filename in ./data/pdb/*.pdb
do
  formula=$(get_formula ${filename})
  mv ${filename} ${filename//.pdb/})_${formula}.pdb
done