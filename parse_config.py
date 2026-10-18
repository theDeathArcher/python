lines = ["port=8080", "host=web1", "debug=false"]
config = {}

for line in lines:
    key, value = line.split("=")
    config[key] = value

print(config)
print(int(config["port"]) + 1)
