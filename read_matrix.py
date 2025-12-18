import yaml

with open("models.yml") as fh:
    config = yaml.safe_load(fh.read())

print(f"{config=}")
