#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 19170307  # 47613
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
