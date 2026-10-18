servers = {"web1": {"ip": "10.0.0.11", "port": 80},
           "db1":  {"ip": "10.0.0.21", "port": 5432}}

for server,service in servers.items():
    print(f"{server} {service['ip']}:{service['port']}")
