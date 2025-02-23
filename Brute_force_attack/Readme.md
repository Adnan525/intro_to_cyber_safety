# Brute Force Attack Demonstration

This repository contains a simple demonstration of how brute force attacks work and why strong security measures are essential. The demo includes a basic Python  flask server that simulates a login system and shows how tools like Hydra can be used to attempt password cracking.

## Components

1. A Python Flask server that simulates a login system
2. A demonstration of Hydra and crunch usage for educational purposes
3. Example password lists and configurations

## Setup Instructions

### 1. Install Required Tools

```bash
# Tested on python 3.12
# Update system
apt update

# Install hydra
apt install hydra

# Install crunch
apt install crunch

# Install Python requirements
pip install -r ../requirements.txt 
```

### 2. Create Password List

Create a simple password list for testing:

```bash
crunch 4 4 0123456789 > brute_force.txt
```

### 3. Running the Demo

1. Start the server:
```bash
python target_server.py
```

2. Test with curl (in a new terminal):
```bash
# Test with correct code
# Will receive 'Login successful!'
curl -X POST -d "code=1623" http://localhost:5000/login

# Test with wrong code
# Will receive 'Invalid code'
curl -X POST -d "code=1234" http://localhost:5000/login
```

3. Run the brute force demonstration:
```bash
hydra -I -vV -l user -P brute_force.txt localhost -s 5000 http-post-form "/login:code=^PASS^:Invalid"
```
  
Output:
```bash
[ATTEMPT] target localhost - login "user" - pass "1631" - 1632 of 10000 [child 5] (0/0)
[ATTEMPT] target localhost - login "user" - pass "1632" - 1633 of 10000 [child 10] (0/0)
[ATTEMPT] target localhost - login "user" - pass "1633" - 1634 of 10000 [child 9] (0/0)
[ATTEMPT] target localhost - login "user" - pass "1634" - 1635 of 10000 [child 11] (0/0)
[ATTEMPT] target localhost - login "user" - pass "1635" - 1636 of 10000 [child 4] (0/0)
[ATTEMPT] target localhost - login "user" - pass "1636" - 1637 of 10000 [child 2] (0/0)
[5000][http-post-form] host: localhost   login: user   password: 1623
[STATUS] attack finished for localhost (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-02-23 14:07:35

```

## Understanding the Hydra Command

The Hydra command breaks down as follows:
- `-vV`: Very verbose
- `-I`: Don't restore previous session
- `-t 1`: Use only 1 thread (did not use in the demo) 
- `-l user`: Username (required by Hydra but not used in our demo)
- `-P brute_force.txt`: Password list file
- `localhost`: Target server
- `-s 5000`: Port number
- `http-post-form`: Type of form submission(post request)
- `"/login:code=^PASS^:Invalid"`: Attack format
  - `/login`: The endpoint
  - `code=^PASS^`: The form field where ^PASS^ is replaced with each attempt
  - `Invalid`: The failure message to look for

## Educational Purpose Notice

**IMPORTANT**: This demonstration is created strictly for educational purposes to help understand:
- How brute force attacks work
- Why strong passwords are important
- The need for security measures like:
  - Rate limiting
  - Account lockouts
  - Multi-factor authentication
  - Complex password requirements

Do not use these techniques against any systems without explicit written permission. Unauthorized attacks against computer systems are illegal and unethical.

## Security Best Practices

To protect against such attacks in real systems, implement:
1. Rate limiting
2. Account lockout policies
3. Complex password requirements
4. Multi-factor authentication
5. Security logging and monitoring
6. IP-based blocking
7. CAPTCHA or similar human verification

Remember: Understanding security vulnerabilities is important for building better defenses, but should never be used for malicious purposes.
