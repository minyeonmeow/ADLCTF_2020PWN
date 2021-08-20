#! /bin/bash

for d in */docker/share/flag; do
    printf "%-40s %s\n" "$d" "$(<$d)"
done
