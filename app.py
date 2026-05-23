from flask import Flask
from flask import request

from kiteconnect import KiteConnect

app = Flask(__name__)

# ==========================================
# API DETAILS
# ==========================================

API_KEY = "i2c07s753rdi06u5"

API_SECRET = "i8pmxc6eij1kz07isa6qmk1br3y7nimc"

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    kite = KiteConnect(
        api_key=API_KEY
    )

    login_url = kite.login_url()

    return f"""

    <h1>
    Zerodha Token Generator
    </h1>

    <a href="{login_url}">
    CLICK HERE TO LOGIN
    </a>

    """

# ==========================================
# CALLBACK
# ==========================================

@app.route("/callback")
def callback():

    try:

        request_token = request.args.get(
            "request_token"
        )

        kite = KiteConnect(
            api_key=API_KEY
        )

        data = kite.generate_session(
            request_token,
            api_secret=API_SECRET
        )

        access_token = data[
            "access_token"
        ]

        return f"""

        <h1>
        ACCESS TOKEN GENERATED
        </h1>

        <textarea
        rows="10"
        cols="100"
        >
{access_token}
        </textarea>

        """

    except Exception as e:

        return f"""

        <h1>
        ERROR
        </h1>

        <pre>
        {str(e)}
        </pre>

        """

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
