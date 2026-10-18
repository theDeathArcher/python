line = "2026-10-14 13:45:01 ERROR disk check failed"

date = line.strip().split()[0]
hour = line.strip().split()[1].strip().split(":")[0]
severity = line.strip().split()[2]

print(f"{date} {hour} {severity}")
