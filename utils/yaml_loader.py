import yaml

def load_tool_config(filepath):

    with open(filepath, "r") as file:

        config = yaml.safe_load(file)

    return config