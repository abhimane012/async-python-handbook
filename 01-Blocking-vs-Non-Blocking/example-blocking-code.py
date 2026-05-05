# Blocking code example in Python

import time

print("Task 1 started")

# This is a blocking operation
# Program will wait here until sleep finishes
time.sleep(5)

print("Task 1 finished")

print("Task 2 started")
print("Task 2 finished")
