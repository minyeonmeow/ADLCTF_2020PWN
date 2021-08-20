#! /bin/bash

# signal handler
trap "exit 1" SIGINT

for d in */; do
    name=$(ls "$d" | grep "\(pay\|sol\|crack\).*\.py$")

    if (( $(echo -e "$name" | wc -l) > 1 )); then
        # filter out old or tmp scripts
        name=$(echo -e "$name" | grep -v "\(old\|tmp\|temp\)")
    fi

    printf "\n%s\n" "==================== Testing $d:"
    if [ -n $name ]; then
        cd "$d"
        if [ -x "$name" ]; then
            set -x
            "./$name"
            set +x
        else
            set -x
            python3 "./$name"
            set +x
        fi
        cd -
    fi
done
