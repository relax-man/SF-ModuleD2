import sentry_sdk
import os
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

SENTURY_URL = "https://4dcd700347cf44b7a0278bc70bf8c3d2@o462867.ingest.sentry.io/5467390"

sentry_sdk.init(
    SENTURY_URL,
    traces_sample_rate=1.0,
    integrations=[BottleIntegration()]
)

@route("/")
def hello_page():
    return HTTPResponse(status=200, body="Hello!")

@route("/success")
def sucess_page():
    return HTTPResponse(status=200, body="OK")

@route('/fail')
def get_error():
    raise RuntimeError('Server error')


if __name__ == "__main__":

    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
