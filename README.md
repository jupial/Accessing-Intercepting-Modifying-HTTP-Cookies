# Cookie Monster: Signed, But Not Safe (CTF)

## Description
This Capture The Flag (CTF) challenge demonstrates how insecure handling of HTTP cookies can lead to privilege escalation.

The application stores user roles inside a signed cookie, but uses a weak secret. This allows attackers to modify the cookie and escalate their privileges to access protected resources.

Your goal is to escalate privileges from a normal user to an admin and retrieve the flag.

## Run with Docker (Recommended)

1. Clone the repository:

git clone https://github.com/yourusername/cookie-ctf.git
cd cookie-ctf

2. Build the Docker image:

docker build -t cookie-ctf .

3. Run the Docker container:

docker run -p 5000:5000 cookie-ctf

4. Open your browser and go to:

http://localhost:5000

You should now see the CTF interface with login and admin links.
