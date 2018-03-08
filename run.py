import os

from app import app


# app = app(os.environ.get("app_config"))

if '__main__' == __name__:
    app.run()