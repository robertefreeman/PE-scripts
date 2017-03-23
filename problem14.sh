#Problem 14: Find the longest Collatz Chain of a number <= 1000000


#!/bin/bash

maxS=1
startN=800000
solution=1

function seqCount {
	local seqC=1
	local seqN=$1
	while [ $seqN -ne 1 ] 
		do
		eval=$(( seqN % 2 ))
		if [ $eval -eq 0 ]
		then
			seqN=$((seqN/2))
		else
			seqN=$((seqN*3+1))
		fi
		seqC=$((seqC+1))
	done 
	if [ $seqC -gt $maxS ]
	then
		maxS=$seqC
		solution=$1
	fi
} 

function findSolution {
	local maxN=$1
	while [ $startN -lt $maxN ]
		do
		seqCount $startN
		startN=$((startN+1))
	done
}

start=`date +%s.%N`
findSolution 1000000
end=`date +%s.%N`
runtime=$(bc <<< "${end} - ${start}")

echo "Found: $solution with a Chain of: $maxS in $runtime seconds"

