import os
try:
    from App.app import create_app
except ModuleNotFoundError:
    from app import create_app


app = create_app(os.environ.get("app_config"))

if '__main__' == __name__:
    app.run()