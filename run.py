from flask_webgoat import create_app

app = create_app()


# version 2.0

@app.after_request
def add_csp_headers(response):
    # vulnerability: Security Misconfiguration
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-inline'"
    return response

if __name__ == '__main__':
    app.run()
