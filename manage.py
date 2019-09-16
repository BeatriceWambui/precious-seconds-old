from app import create_app,db
from flask_script import Manager,Server

app = create_app('development')
manager = Manager(app)
manager.add_command('runserver',Server)

@manager.shell
def shell_context():
    return {'db':db}
if __name__ == '__main__':
    manager.run()