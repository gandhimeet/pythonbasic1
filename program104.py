"""
Write a Python program to get the effective group id, effective user id, real group id, and a list of supplemental groupids associated with the current process.
Note: Availability: Unix.
"""

import os

print("Effective group id:", os.getegid())
print("Effective user id:", os.geteuid())
print("Real group id:", os.getgid())
print("List of supplemental group ids:", os.getgroups())
