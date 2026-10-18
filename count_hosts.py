hosts = ["web1", "db1", "web1", "web2", "db1", "web1"]
counts = {}

for host in hosts:
    counts[host] = counts.get(host,0) + 1

print(sorted(counts))

most_frequent = ""
most_count = 0

for host,count in counts.items():
    if count > most_count:
        most_count = count
        most_frequent = host

print(f"Host {most_frequent} appears {most_count} times")
