# FILE: vulnerable_server.py
# ROLE: The "Victim" Application
# VULNERABILITY: Critical Remote Code Execution (RCE)

import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running. Endpoint: /diagnose?host=<ip>"

@app.route('/diagnose', methods=['GET'])
def network_diagnostics():
    # SCENARIO: A tool for admins to ping servers.
    target_host = request.args.get('host')
    
    if not target_host:
        return "Error: No host provided", 400

    # FLAW: The app trusts the user input directly in a shell command.
    # An attacker can append "; calc.exe" (Windows) or "; ls" (Linux).
    command = f"ping -n 1 {target_host}"
    
    try:
        # EXECUTION: shell=True enables command chaining.
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return f"<pre>{output.decode('utf-8')}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"

if __name__ == '__main__':
    # We run on port 5000
    print("[-] Starting Vulnerable Server on port 5000...")
    app.run(debug=True, port=5000)