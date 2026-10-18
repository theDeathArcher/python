service_ports = { "ssh":22, "http":80, "https":443, "postgres":5432 }

service=input("What service port are you looking for?\nService : ")
if service in service_ports:
    print(f"Port of service {service} is: {service_ports[service]}")
else:
    print(f"unknown service: {service}")
