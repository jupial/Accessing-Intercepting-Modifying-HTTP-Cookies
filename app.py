import os
import base64
import hashlib
import json
from flask import Flask, request, render_template

app = Flask(__name__)

SECRET = "123"  # intentionally weak (CTF vulnerability)
FLAG = "FLAG{cookie_tampering_master}"

# -------------------------
# SAFE COOKIE PARSING (FIXED CRASHES)
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

        parts = cookie.split(".")
        if len(parts) != 2:
            return None

        b64, sig = parts

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

    if not data:
        data = {"role": "guest"}

    return render_template("index.html", role=data.get("role", "guest"))


@app.route('/login')
def login():
    session_cookie = encode_session({"role": "user"})
    resp = redirect('/')
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
    app.run(host="0.0.0.0", port=5000)
@app.route('/login')
def login():
    session = encode_session({"role": "user"})
    resp = make_response(redirect('/'))
    resp.set_cookie("session", session)
    return resp

@app.route('/admin')
def admin():
    cookie = request.cookies.get("session")
    data = decode_session(cookie)
   
    current_role = data.get("role", "guest") if data else "guest"

    if current_role == "admin":
        return render_template("admin.html", flag=FLAG)

    return render_template("unauthorized.html", role=current_role), 403
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

SECRET = os.environ.get("CHALLENGE_SECRET", "123")
