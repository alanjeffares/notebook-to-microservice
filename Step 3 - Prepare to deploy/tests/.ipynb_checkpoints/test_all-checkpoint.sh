#!/bin/sh

for test in tests/unit/test_*.py
do
    python3 "${test}" -v
    RESULT=$?
    if [ $RESULT -ne 0 ]; then
        echo "failed $CMD"
        exit 1
    fi
done
echo "Passed unit tests"


pycodestyle ./src/
RESULT=$?
if [ $RESULT -ne 0 ]; then
    echo "failed $CMD"
    exit 1
fi
echo "Passed linting"