# FILE: secure_server.py
# ROLE: The "Secure" Application
# STATUS: Patched against OWASP A03 (Injection)

import subprocess
import platform
from flask import Flask, request

app = Flask(__name__)

@app.route('/diagnose', methods=['GET'])
def network_diagnostics():
    target_host = request.args.get('host')
    
    if not target_host:
        return "Error: No host provided", 400

    # FIX 1: Input Validation (The Filter)
    # We explicitly allow ONLY alphanumeric chars, dots, and hyphens.
    # If the user tries to send "&", "|", or ";", we block it immediately.
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    if not set(target_host).issubset(allowed_chars):
        print(f"[SECURITY BLOCK] Malicious input detected: {target_host}")
        return "Security Alert: Invalid characters detected.", 403

    # FIX 2: Secure Execution Architecture
    # Check OS to choose correct ping flag (-n for Windows, -c for Linux)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # CRITICAL FIX: Pass command as a LIST. Do NOT use shell=True.
    # This creates a wall between the command and the user input.
    command = ['ping', param, '1', target_host]
    
    try:
        output = subprocess.check_output(command, shell=False, stderr=subprocess.STDOUT)
        return f"<pre>{output.decode('utf-8')}</pre>"
    except subprocess.CalledProcessError:
        return "Ping failed (Host unreachable)."
    except FileNotFoundError:
        return "System Error: Ping command not found."

if __name__ == '__main__':
    print("[-] Starting SECURE Server on port 5000...")
    # FIX 3: Disable Debug Mode
    app.run(debug=False, port=5000)