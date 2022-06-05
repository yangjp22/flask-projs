from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app
from exts import db
from apps.user.models import User
# generate an app
app = create_app()

# generate a manager instance
manager = Manager(app)

# connect the app and SQLAlchemy ORM
Migrate(app, db)

# adding command for CML
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()