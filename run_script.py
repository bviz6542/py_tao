import sys
import subprocess
import glob

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run_script.py <python file name>")
        sys.exit(1)
    
    script_name = sys.argv[1]
    script_files = glob.glob(f"{script_name}.py")
    if not script_files:
        print(f"File {script_name}.py not found.")
        sys.exit(1)
    script_file = script_files[0]

    input_filename = 'input.txt'
    try:
        with open(input_filename, 'r') as f:
            input_data = f.read()
    except FileNotFoundError:
        print(f"Input file {input_filename} not found.")
        sys.exit(1)

    process = subprocess.Popen([sys.executable, script_file], stdin=subprocess.PIPE)
    process.communicate(input=input_data.encode())

if __name__ == "__main__":
    main()
