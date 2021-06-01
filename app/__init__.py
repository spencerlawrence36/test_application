from flask import Flask
from config import Config
from celery import Celery
from flask_socketio import SocketIO

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
socketio = SocketIO()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    if app.debug:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    socketio.init_app(app, cors_allowed_origins='*')

    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_BACKEND_URL'],
        broker=app.config['CELERY_BROKER_URL']
    )

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    from app.main import main_bp

    app.register_blueprint(main_bp)


    return app
