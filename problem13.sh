#Problem #13	Work out the first ten digits of the sum of the provided one-hundred 50-digit numbers.

#!/bin/bash

#provided number file
file="./p13/data.txt"
nums=[]

#create list of numbers from provided file
function listMaker {
  while read -r line; do
    nums=("${nums[@]}" $line)
  done <"$file"
}

#sum the numbers in the list
function sumList {
	totVal=0
	for x in {1..100}
	do
		indVal=${nums[$x]} 
		totVal=$(bc <<< "${totVal} + ${indVal}")
	done
}

#Split off the first ten numbers of the sum
function firstTen {
	totVal=$(cut -c1-10 <<< $totVal)  	
}


#call functions and record runtime

start=`date +%s.%N`
listMaker
sumList
firstTen
end=`date +%s.%N`
runtime=$(bc <<< "${end} - ${start}")

echo "Found the solution: $totVal in $runtime seconds"

