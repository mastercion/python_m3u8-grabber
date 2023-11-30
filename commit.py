import subprocess

def run_git_commands():
    try:
        # Add all changes to the staging area
        subprocess.run(["git", "add", "*"], check=True)

        # Commit changes with a predefined commit message
        commit_message = "Your commit message here"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        print("Git add and commit executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

run_git_commands()