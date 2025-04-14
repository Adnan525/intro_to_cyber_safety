import subprocess

def run_command():
    user_input = input("What is your name? ")
    command = f"echo Hi {user_input}!"
    # This is a potential command injection vulnerability
    subprocess.run(command, shell=True, text=True)
    
    # To prevent command injection, use a safer method:
    # subprocess.run(["echo", f"Hi {user_input}!"], shell=False, text=True)

if __name__ == "__main__":
    run_command()