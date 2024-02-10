#!/bin/bash

# Start the first process
python ./main.py &

# Start the second process
python ./posting.py &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
