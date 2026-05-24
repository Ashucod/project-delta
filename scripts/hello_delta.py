# Project Delta - Hello World
# Author: Ashish Shinde | Date: 2026-05-19
import datetime
import os

print("=" * 50)
print(f"PROJECT DELTA - SYSTEM ONLINE")
print("=" * 50)
print(f" Boot Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(" Status: Pre-season Training Camp ACTIVE")
print(" Objective: HFT Bot. No shortcuts. No excuses.")
print("=" * 50)

# This is Day 2 of the git and github training. We will practice basic git commands and build muscle mermory for it.
def run_diagnostics():
    print("=== SYSTEM DIAGNOSTICS ===")
    print(f"Working Directory : {os.getcwd()}")
    print(f"OS Type           : {os.name}")
    print(f"Logged in as      : {os.getlogin()}")
    print(f"PATH              : {os.environ.get('PATH')}")
    print("==========================")

run_diagnostics()
print("Hello, Delta Team! Let's crush it this season!")