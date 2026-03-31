import json

# Define the configuration directly since we don't have yaml module
config = [
    {
        "label": "antani",
        "models": ["a", "b", "c"],
        "timeout": 300
    }
]

# Convert to JSON format expected by GitHub Actions
matrix_config = json.dumps(config)
print(f"config={matrix_config}")