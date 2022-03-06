from os import getenv
from flask import Flask, request, render_template


app = Flask("myApp")


@app.route('/', methods=['GET'])
def score_server():
    REGION = getenv('REGION', 'us-west-1')
    ENV_NAME = getenv('ENV_NAME', 'PRODUCTION')
    if request.method == 'GET':
        return f"""
          <html>
          <head>
              <title>{ENV_NAME}</title>
          </head>
          <body>
            <h1>The ENV_NAME is {ENV_NAME} </h1>
            <h2>The REGION is {REGION} </h2>
          </body>
          </html>
          """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
