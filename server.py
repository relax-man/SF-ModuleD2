import sentry_sdk
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    "https://f6fb9c7e9f1c4aa0901d9f7ba610a738@o462795.ingest.sentry.io/5466698",
    traces_sample_rate=1.0,
    integrations=[BottleIntegration()]
)

@route("/")
def hello_page():
    return HTTPResponse(status=200, body="Hello!")

@route("/success")
def sucess_page():
    return HTTPResponse(status=200, body="Sucessfully operation")

@route('/fail')
def get_error():
    raise RuntimeError('Server error for the test')


if __name__ == "__main__":

    run(
        host='0.0.0.0',
        port=5000,
        server='gunicorn',
        workers=3
    )
