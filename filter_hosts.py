hosts = ["web1", "db1", "web2", "cache1"]
web_hosts = []

for host in hosts:
    if host.startswith("web"):
        web_hosts.append(host)

print(f"there are { len(web_hosts) } web hosts, namely: { web_hosts }")
