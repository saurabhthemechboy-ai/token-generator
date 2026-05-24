from flask import Flask
from flask import request
from flask import redirect

from kiteconnect import KiteConnect

import os

app = Flask(__name__)

# ==========================================
# API DETAILS
# ==========================================

API_KEY = os.getenv(
    "KITE_API_KEY"
)

API_SECRET = os.getenv(
    "KITE_API_SECRET"
)

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return """

    <h1>
    Zerodha Token Generator
    </h1>

    <br>

    <a href="/login">
    LOGIN TO ZERODHA
    </a>

    """

# ==========================================
# LOGIN
# ==========================================

@app.route("/login")
def login():

    kite = KiteConnect(
        api_key=API_KEY
    )

    return redirect(
        kite.login_url()
    )

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

        <h2>
        ACCESS TOKEN
        </h2>

        <textarea rows="8" cols="100">
        {access_token}
        </textarea>

        """

    except Exception as e:

        return f"""

        <h2>
        ERROR:
        {str(e)}
        </h2>

        """

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
