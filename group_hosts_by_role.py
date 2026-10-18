roles = {"web1": "web", "web2": "web", "db1": "db", "cache1": "cache"}
groups = {}

for host,role in roles.items():
    if role not in groups:
        groups[role] = []
    
    groups[role].append(host)

print(groups)
