# NOTE: https://owasp.org/www-community/attacks/Session_hijacking_attack
# NOTE: https://www.youtube.com/watch?v=RlSweA5UfYw

from flask import Flask, request, make_response, redirect, render_template_string
import secrets
import time
import hashlib

app = Flask(__name__)

USERS = {"student": "password123"}
sessions = {}
secure_sessions = {}


def get_browser_fingerprint():
    fingerprint_data = [
        request.user_agent.string,
        request.accept_languages,
        request.accept_charsets,
        request.accept_encodings,
    ]
    fingerprint = hashlib.sha256(''.join(str(d) for d in fingerprint_data).encode()).hexdigest()
    print(f"\n🔍 Browser Fingerprint Generated:")
    print(f"   User-Agent: {request.user_agent.string}")
    print(f"   Generated Fingerprint: {fingerprint[:16]}...")
    return fingerprint


HTML = """
<!DOCTYPE html>
<html>
<body style="padding: 20px; font-family: Arial;">
    <h2>Session Demo: {{ version }}</h2>

    {% if user %}
        <div style="background: #e8f5e9; padding: 15px; border-radius: 5px;">
            <p>Welcome, <b>{{ user }}</b>!</p>
            <p>Your session ID: <b>{{ session_id }}</b></p>
            {% if is_secure %}
                <p>Session expires in: {{ expiry }} seconds</p>
                <p>Browser fingerprint: {{ fingerprint[:16] }}...</p>
            {% endif %}
        </div>
        <br>
        <a href="{{ '/secure/logout' if is_secure else '/vulnerable/logout' }}">Logout</a>
    {% else %}
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Login">
        </form>
        <p>Use: student / password123</p>
    {% endif %}

    <hr>
    <p>Try: <a href="/vulnerable">Vulnerable Version</a> | <a href="/secure">Secure Version</a></p>
</body>
</html>
"""


@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    print("\n🔓 Vulnerable Version Access:")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"   Login Attempt - Username: {username}")

        if USERS.get(username) == password:
            session_id = secrets.token_hex(8)
            sessions[session_id] = username
            print(f"   ✅ Login Successful")
            print(f"   Generated Session ID: {session_id}")

            response = make_response(redirect('/vulnerable'))
            response.set_cookie('session_id', session_id)
            return response
        print(f"   ❌ Login Failed - Invalid Credentials")

    session_id = request.cookies.get('session_id')
    if session_id:
        print(f"   Checking Session ID: {session_id}")

    user = sessions.get(session_id)
    if user:
        print(f"   ✅ Valid Session Found for User: {user}")
    else:
        print(f"   ❌ No Valid Session Found")

    return render_template_string(HTML,
                                  version="Vulnerable Version",
                                  user=user,
                                  session_id=session_id,
                                  is_secure=False)


@app.route('/secure', methods=['GET', 'POST'])
def secure():
    print("\n🔒 Secure Version Access:")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"   Login Attempt - Username: {username}")

        if USERS.get(username) == password:
            session_id = secrets.token_hex(32)
            fingerprint = get_browser_fingerprint()

            secure_sessions[session_id] = {
                'username': username,
                'fingerprint': fingerprint,
                'created_at': time.time()
            }

            print(f"   ✅ Login Successful")
            print(f"   Generated Session ID: {session_id}")
            print(f"   Session Bound to Fingerprint: {fingerprint[:16]}...")

            response = make_response(redirect('/secure'))
            response.set_cookie(
                'session_id',
                session_id,
                httponly=True,
                samesite='Strict',
                max_age=300
            )
            return response
        print(f"   ❌ Login Failed - Invalid Credentials")
        return redirect('/secure')

    session_id = request.cookies.get('session_id')
    if session_id:
        print(f"   Checking Session ID: {session_id}")

    session = secure_sessions.get(session_id)
    user = None
    expiry = None
    fingerprint = None

    if session:
        print("   Session Found, Validating...")
        current_time = time.time()
        current_fingerprint = get_browser_fingerprint()
        session_age = current_time - session['created_at']

        print(f"   Session Age: {session_age:.1f} seconds")
        print(f"   Original Fingerprint: {session['fingerprint'][:16]}...")
        print(f"   Current Fingerprint: {current_fingerprint[:16]}...")

        # Validate session with fingerprint
        if session_age > 300:
            print(f"   ❌ Session Expired (Age: {session_age:.1f}s)")
            del secure_sessions[session_id]
        elif session['fingerprint'] != current_fingerprint:
            print(f"   ❌ Fingerprint Mismatch - Possible Session Hijacking Attempt!")
            del secure_sessions[session_id]
        else:
            print(f"   ✅ Valid Session - All Checks Passed")
            user = session['username']
            expiry = int(300 - session_age)
            fingerprint = session['fingerprint']
    else:
        print("   ❌ No Session Found")

    return render_template_string(HTML,
                                  version="Secure Version",
                                  user=user,
                                  session_id=session_id,
                                  is_secure=True,
                                  expiry=expiry,
                                  fingerprint=fingerprint)


@app.route('/vulnerable/logout')
def vulnerable_logout():
    print("\n👋 Vulnerable Version Logout:")
    session_id = request.cookies.get('session_id')
    if session_id in sessions:
        print(f"   Removing Session: {session_id}")
        del sessions[session_id]
    response = make_response(redirect('/vulnerable'))
    response.delete_cookie('session_id')
    return response


@app.route('/secure/logout')
def secure_logout():
    print("\n👋 Secure Version Logout:")
    session_id = request.cookies.get('session_id')
    if session_id in secure_sessions:
        print(f"   Removing Session: {session_id}")
        del secure_sessions[session_id]
    response = make_response(redirect('/secure'))
    response.delete_cookie('session_id')
    return response


@app.route('/')
def root():
    return redirect('/vulnerable')


if __name__ == '__main__':
    app.run(debug=True)