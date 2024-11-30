import yaml  # Assuming you are using PyYAML for YAML handling

def load_yaml(file_path: str):
    """Load a YAML file and return its contents."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
