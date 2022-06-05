from exts import db
from apps import create_app
from flask_script import Manager, Shell
from models import *
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app=app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, History=History, Details=Details)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    # manager.run()
    app.run()
