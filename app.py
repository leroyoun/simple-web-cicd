"""
Simple Flask Web App - CI/CD Demo
"""
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Flask App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .card {
            background: #fff; border-radius: 16px; padding: 48px 40px;
            max-width: 500px; width: 90%; box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 { color: #333; font-size: 28px; margin-bottom: 8px; }
        .version { color: #764ba2; font-size: 14px; font-weight: 600; margin-bottom: 24px; }
        .status { display: inline-block; background: #e8f5e9; color: #2e7d32;
                  padding: 6px 16px; border-radius: 20px; font-size: 14px; margin-bottom: 24px; }
        .info { background: #f5f5f5; border-radius: 8px; padding: 16px;
                text-align: left; font-size: 13px; color: #666; line-height: 1.8; }
        .info span { color: #333; font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <h1>CI/CD Auto Deploy Success</h1>
        <p class="version">Flask App v2.0 | Python {{ python_version }}</p>
        <div class="status">Server Running</div>
        <div class="info">
            <p><span>Host ID:</span>{{ hostname }}</p>
            <p><span>Deploy Time:</span>{{ deploy_time }}</p>
            <p><span>Environment:</span>{{ environment }}</p>
            <p><span>Student ID:</span>2440666136</p>
            <p><span>Name:</span>Lai Yangyuan</p>
        </div>
    </div>
</body>
</html>"""

@app.route("/")
def index():
    import socket, platform, datetime
    return render_template_string(
        HTML,
        python_version=platform.python_version(),
        hostname=socket.gethostname(),
        deploy_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment="Production" if app.config.get("ENV") == "production" else "Development",
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
