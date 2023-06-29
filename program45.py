'''
Write a Python program that calls an external command.
'''
#importing subprocess module 
import subprocess

def call_external_command(command):
    try:
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        
        # Print the output
        print(output)
    except subprocess.CalledProcessError as e:
        # An error occurred
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error message: {e.output}")
        
# Example usage
command = "ls -l"
call_external_command(command)
