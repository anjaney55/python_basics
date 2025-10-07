import os

for i in range(1,21):
    os.rename(f"Tutorials/Day{i}", f"Tutorials/Day {i}")  # we can rename all folders using source and dest