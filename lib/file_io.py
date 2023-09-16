def write_file(file_name, content):
    """Write content to a file."""
    with open(file_name, 'w') as f:
        f.write(content)

def append_file(file_name, content):
    """Append content to a file."""
    with open(file_name, 'a') as f:
        f.write(content)

def read_file(file_name):
    """Read content from a file and return it."""
    with open(file_name, 'r') as f:
        return f.read()
