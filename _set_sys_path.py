import subprocess
import sys

def set_syspath_location():
    # Run the command and capture the output
    result = subprocess.run(['pip', 'show', 'pip'], capture_output=True, text=True)
    
    # Split the output into lines
    lines = result.stdout.splitlines()
    
    # Extract the Location line
    for line in lines:
        if line.startswith('Location:'):
            location = line.split(' ', 1)[1]  # Get the value after 'Location:'
            return location

location = set_syspath_location()
sys.path.append(location)
print(f"sys.path updated to: {location}")
