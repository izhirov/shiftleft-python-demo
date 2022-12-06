from flask_webgoat import create_app

app = create_app()


@app.after_request
def add_csp_headers(response):
    return response

if __name__ == '__main__':
    app.run()
