# Cookie Monster: Signed, But Not Safe (CTF)

## Description
This Capture The Flag (CTF) challenge demonstrates how insecure handling of HTTP cookies can lead to privilege escalation.

The application stores user roles inside a signed cookie, but uses a weak secret. This allows attackers to modify the cookie and escalate their privileges to access protected resources.

Your goal is to escalate privileges from a normal user to an admin and retrieve the flag.

## Run with Docker (Recommended)

1. Clone the repository:

```bash
git clone https://github.com/jupial/Accessing-Intercepting-Modifying-HTTP-Cookies.git
cd Accessing-Intercepting-Modifying-HTTP-Cookies
docker build -t cookie-ctf .
docker run -p 5001:5000 cookie-ctf
```
 

You should now see the CTF interface.
