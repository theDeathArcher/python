shells_counter = {}

with open("/etc/passwd") as f:
    for line in f:
        parts = line.strip().split(":")
        
        shell = parts[-1]
        shells_counter[shell] = shells_counter.get(shell,0) + 1

for shell, count in shells_counter.items():
    print(f"{shell} is the login shell of {count} accounts.")
