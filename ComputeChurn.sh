#!/bin/bash

# arg1: folder where the code is.
# arg2: last n months to perform the churn analysis.
# arg3: take only n more frequent files.
cd "$1"

# TEST only Kernel project 
# git log --format=format: --name-only --since=$2.month | egrep -v '^$' | grep 'Alma3D Kernel/.*\.cpp$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1,\2/' | sort -nr | head -$3

# ALL codebase
# git log --format=format: --name-only --since=$2.month | egrep -v '^$' | grep '.*\.cpp$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1,\2/' | sort -nr | head -$3
git log --format=format: --name-only --since=$2.month | egrep -v '^$' | egrep '.*\.(cpp|cc|c)$' | sort | uniq -c | sed 's/^\s*\([0-9]*\) \(.*\)$/\1;\2/' | sort -nr

