from app import app

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My DevOps Flask Site</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                padding: 30px;
                backdrop-filter: blur(10px);
            }
            h1 { color: #ffd700; }
            .tech-badge {
                display: inline-block;
                background: #2c3e50;
                padding: 5px 10px;
                margin: 5px;
                border-radius: 5px;
                font-size: 12px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to My DevOps Journey</h1>
            <p>I'm a developer who knows:</p>
            <div>
                <span class="tech-badge">C#</span>
                <span class="tech-badge">Java</span>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">JavaScript</span>
                <span class="tech-badge">Docker</span>
                <span class="tech-badge">Kubernetes</span>
                <span class="tech-badge">Jenkins</span>
                <span class="tech-badge">GitHub</span>
            </div>
            <p>This site runs on <strong>Flask + Docker + GitHub Codespaces</strong></p>
            <p>📅 Server time: <span id="time"></span></p>
        </div>
        <script>
            setInterval(() => {
                document.getElementById('time').innerText = new Date().toLocaleString();
            }, 1000);
        </script>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {"status": "healthy", "platform": "Codespaces"}

@app.route('/devops-tools')
def devops_tools():
    tools = ["Docker", "K8s", "Jenkins", "GitHub Actions", "Terraform"]
    return {"tools": tools, "count": len(tools)}