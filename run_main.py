import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError:
        print(f"An error occurred while executing {script_name}.")

run_script("hekll.py")
run_script("make_format_entry.py")
