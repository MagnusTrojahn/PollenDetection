import subprocess

def execute_shell_command(command):
    # Run the shell command
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')

    # Check the return code
    if result.returncode == 0:
        # Command executed successfully
        print("Command executed successfully!")
        # Print the command output
        print(result.stdout)
    else:
        # Command execution failed
        print("Command execution failed!")
        # Print the error message
        print(result.stderr)

# Example usage
command = "yolo detect train model=yolov8x.pt data=C:/Users/magnu/Desktop/Pollendetection/v3/data.yaml epochs=10 imgsz=640 batch=8 project=C:/Users/magnu/Desktop/Pollendetection/v3/training_results name=pollen"

if __name__ == "__main__":
    execute_shell_command(command)
