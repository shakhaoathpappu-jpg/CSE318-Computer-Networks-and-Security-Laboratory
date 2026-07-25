import time
import os

os.system("cls" if os.name == "nt" else "clear")

print("Initializing virus...")
time.sleep(1)

for i in range(0, 101, 10):
    print(f"Deleting files... {i}%")
    time.sleep(0.4)

print("\nERROR: Critical system failure!")
time.sleep(2)

print("\n😁 Just kidding! No files were deleted.")