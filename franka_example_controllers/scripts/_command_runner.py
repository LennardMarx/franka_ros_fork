#!/usr/bin/env python

import subprocess

def execute_shell_command(command):
    try:
        # Execute the shell command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Decode the output and error (if any)
        output = result.stdout.decode('utf-8')
        error = result.stderr.decode('utf-8')
        
        return output, error
    except subprocess.CalledProcessError as e:
        # Handle errors in the execution
        return None, str(e)

if __name__ == "__main__":
    command = "rosrun controller_manager controller_group switch force"
    output, error = execute_shell_command(command)

    if output:
        print("Command Output:\n", output)
    if error:
        print("Command Error:\n", error)
