#!/bin/bash

echo 1st parameter: "$1"


# TEST only Kernel project 
# git log --format=format: --name-only --since=$2.month | egrep -v '^$' | grep 'Alma3D Kernel/.*\.cpp$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1,\2/' | sort -nr | head -$3

# ALL codebase
# git log --format=format: --name-only --since=$2.month | egrep -v '^$' | grep '.*\.cpp$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1,\2/' | sort -nr | head -$3
#git log --format=format: --name-only --since=$2.month | egrep -v '^$' | egrep '.*\.(cpp|cc|c)$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1,\2/' | sort -nr

