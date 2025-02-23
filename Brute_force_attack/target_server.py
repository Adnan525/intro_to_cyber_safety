from flask import Flask, request
import time

app = Flask(__name__)


def check_code(code):
    """
    Check if the code is valid
    Args:
        code: code to check
    Returns:
        True if the code is valid, False otherwise
    """
    return code == "1623"


@app.route('/login', methods=['POST'])
def login():
    code = request.form.get('code', '')
    print(f"Received: {code}")

    if check_code(code):
        return "Login successful!", 200
    # try other error codes here, 401 will confuse hydra a bit here
    return "Invalid code", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

