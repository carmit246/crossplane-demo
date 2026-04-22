from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    app_env = os.getenv("APP_ENV", "unknown")
    pr_number = os.getenv("PR_NUMBER", "")
    commit_sha = os.getenv("COMMIT_SHA", "unknown")
    hostname = socket.gethostname()

    pr_line = f"<p><b>PR:</b> {pr_number}</p>" if pr_number else ""

    return f"""
    <html>
      <body style="font-family: Arial; padding: 40px;">
        <h1>Demo App</h1>
        <p><b>Environment:</b> {app_env}</p>
        {pr_line}
        <p><b>Commit:</b> {commit_sha}</p>
        <p><b>Pod:</b> {hostname}</p>
      </body>
    </html>
    """

@app.route("/healthz")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
