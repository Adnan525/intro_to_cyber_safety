# Preventing Command Injection in Python

## The Vulnerability in Our Example

The code below contains a command injection vulnerability:

```python
import subprocess

def run_command():
    user_input = input("What is your name? ")
    command = f"echo Hi {user_input}!"
    # This is a potential command injection vulnerability
    subprocess.run(command, shell=True, text=True)

if __name__ == "__main__":
    run_command()
```

## Understanding Command Injection

Command injection occurs when user-supplied input is inserted into a command string and executed by the system shell. When an attacker provides specially crafted input containing shell metacharacters, they can:

- Execute arbitrary commands
- Access sensitive information
- Modify or delete files
- Escalate privileges
- Establish persistent access

## Why `shell=True` is Dangerous

When `shell=True` is specified in Python's subprocess functions:

1. **Shell Interpretation**: The command string is passed to the system shell (`/bin/sh` on Unix or `cmd.exe` on Windows), which interprets special characters.

2. **Command Chaining**: Attackers can use shell operators like `;`, `&&`, `||`, and `|` to execute additional unintended commands.

3. **Special Character Interpretation**: Characters like `>` (redirection), `<` (input redirection), `$` (variable expansion), and backticks (command substitution) are all interpreted by the shell.

4. **Wildcard Expansion**: Characters like `*` and `?` will be expanded by the shell to match files.

## Solution 1: Using `shell=False` (Recommended)

The most secure approach is to avoid the shell entirely by using `shell=False` and passing the command as a list of arguments:

```python
# Secure implementation
subprocess.run(["echo", f"Hi {user_input}!"], shell=False, text=True)
```

### How this prevents command injection:

1. **No Shell Involvement**: The command is executed directly without involving the system shell
2. **Arguments Passed Literally**: Special characters in user input are treated as literal text
3. **No Interpretation**: Shell metacharacters have no special meaning
4. **Direct Execution**: Python directly executes the specified program with the given arguments

## Solution 2: Input Sanitization

If using `shell=True` is absolutely necessary (rarely the case), you must strictly sanitize user input:

```python
import re
import shlex

def sanitize_input(user_input):
    # Option 1: Allow only alphanumeric characters and basic punctuation
    sanitized = re.sub(r'[^\w\s.,!?]', '', user_input)
    return sanitized
    
    # Option 2: Using shlex.quote to escape shell metacharacters
    # return shlex.quote(user_input)

user_input = input("What is your name? ")
sanitized_input = sanitize_input(user_input)
command = f"echo Hi {sanitized_input}!"
subprocess.run(command, shell=True, text=True)
```

### Sanitization approaches:

1. **Allowlist validation**: Only accept characters known to be safe
2. **Character escaping**: Escape special characters using `shlex.quote()`
3. **Blocklist filtering**: Remove or encode known dangerous characters (less secure)

## Solution 3: Use Higher-Level Functions

For many common operations, you can avoid subprocess entirely:

```python
# Instead of using 'echo' via subprocess:
user_input = input("What is your name? ")
print(f"Hi {user_input}!")

# Instead of using 'cat' via subprocess:
with open(filename, 'r') as file:
    content = file.read()
```

## Security Best Practices Summary

1. **Avoid `shell=True`**: Use `shell=False` with a list of arguments
2. **Use proper APIs**: For file operations, networking, etc., use Python's built-in libraries
3. **Sanitize all input**: Validate and sanitize user input even when using `shell=False`
4. **Principle of least privilege**: Run your application with minimal necessary permissions
5. **Input validation**: Validate input before processing (check length, format, content)
6. **Consider subprocess alternatives**: `os.path`, `pathlib`, file I/O operations, etc.

## Why This Matters

Command injection vulnerabilities have led to numerous serious security breaches. They're listed in the OWASP Top 10 security risks and can lead to complete system compromise. Taking the simple step of using `shell=False` with argument lists significantly improves your application's security posture.