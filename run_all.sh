#!/usr/bin/env bash

function ctrl_c()
{
    echo "Caught ctrl-c. Stopping..."
    exit 0
}

trap ctrl_c SIGINT

for D in $(ls `pwd` | sort); do
    case "$D" in
        Problem*.py)
            printf "$D "
            python $D
            ;;
    esac
done
