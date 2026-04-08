# Cookie Monster: Signed, But Not Safe (CTF)

## Description
This Capture The Flag (CTF) challenge demonstrates how insecure handling of HTTP cookies can lead to privilege escalation.

The application uses a cookie-based session system where user roles are stored client-side and protected with a weak signature.

Your goal is to escalate your privileges from a normal user to an admin and retrieve the flag.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cookie-ctf.git
   cd cookie-ctf
