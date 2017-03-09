import os
import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from app.models import db
from config import BASE_DIR, GUNICORN_WORKERS, APPLICATION_URL


file_log = logging.FileHandler(os.path.join(BASE_DIR, 'logs/app_logs.log'))
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s]  * %(message)s',
                    level=logging.DEBUG, handlers=[file_log])


migrate = Migrate(app, db)
manager = Manager(app)


@manager.command
def gunicorn():
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': APPLICATION_URL,
                'workers': GUNICORN_WORKERS
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
