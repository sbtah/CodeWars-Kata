#!/bin/bash


# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other comple

readarray -t my_array <<< "$(echo "${1}" | grep -o .)"


output=''
for genome in "${my_array[@]}"; do
    case "${genome}" in
        A)
            current_genome='T'
            ;;
        T)
            current_genome='A'
            ;;
        C)
            current_genome='G'
            ;;
        G)
            current_genome='C'
            ;;
    esac
    output+="${current_genome}"
done

echo "${output}"