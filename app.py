import os
import base64
import hashlib
import json
from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)

SECRET = os.environ.get("CHALLENGE_SECRET", "123")  # keep weak for CTF
FLAG = "ITC266{cookie_tampering_master}"


# -------------------------
# COOKIE FUNCTIONS
# -------------------------
def encode_session(data):
    json_data = json.dumps(data)
    b64 = base64.b64encode(json_data.encode()).decode()
    sig = hashlib.md5((json_data + SECRET).encode()).hexdigest()
    return f"{b64}.{sig}"


def decode_session(cookie):
    try:
        if not cookie or "." not in cookie:
            return None

        b64, sig = cookie.split(".", 1)

        json_data = base64.b64decode(b64).decode()

        expected_sig = hashlib.md5((json_data + SECRET).encode()).hexdigest()

        if sig != expected_sig:
            return None

        return json.loads(json_data)

    except Exception:
        return None


# -------------------------
# ROUTES
# -------------------------

@app.route('/')
def home():
    cookie = request.cookies.get("session")
    data = decode_session(cookie)

    role = data.get("role", "guest") if data else "guest"

    return render_template("index.html", role=role)


@app.route('/login')
def login():
    session_cookie = encode_session({"role": "user"})
    resp = make_response(redirect('/'))
    resp.set_cookie("session", session_cookie)
    return resp


@app.route('/admin')
def admin():
    cookie = request.cookies.get("session")
    data = decode_session(cookie)

    role = data.get("role", "guest") if data else "guest"

    if role == "admin":
        return render_template("admin.html", flag=FLAG)

    return render_template("unauthorized.html", role=role), 403


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
