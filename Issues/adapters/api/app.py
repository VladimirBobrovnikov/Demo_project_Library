from classic.http_api import App

from application import services

from . import auth, controllers


def create_app(
    is_dev_mode: bool,
    actions: services.ActionsService
) -> App:
    app = App(prefix='/api')
    app.register(controllers.Actions(actions=actions))
    return app
