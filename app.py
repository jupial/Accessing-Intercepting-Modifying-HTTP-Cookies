import os
import base64
import hashlib
import json
from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)

SECRET = "123"  # weak secret (intentional vulnerability)
FLAG = "FLAG{cookie_tampering_master}"

def encode_session(data):
    json_data = json.dumps(data)
    b64 = base64.b64encode(json_data.encode()).decode()
    sig = hashlib.md5((json_data + SECRET).encode()).hexdigest()
    return f"{b64}.{sig}"

def decode_session(cookie):
    try:
        b64, sig = cookie.split(".")
        json_data = base64.b64decode(b64).decode()

        valid_sig = hashlib.md5((json_data + SECRET).encode()).hexdigest()

        if sig != valid_sig:
            return None

        return json.loads(json_data)
    except:
        return None

@app.route('/')
def home():
    cookie = request.cookies.get("session")
    data = decode_session(cookie) if cookie else {"role": "guest"}
    return render_template("index.html", role=data.get("role", "guest"))

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
