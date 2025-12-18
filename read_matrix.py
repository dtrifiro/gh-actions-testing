import yaml

with open("list.yml") as fh:
    config = yaml.safe_load(fh.read())

print(f"{config=}")
