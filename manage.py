import os, sys
from flask.ext.script import Manager, Server, Shell
from MMCS_Survey import app, db
import model


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, model=model)

if __name__ == "__main__":
    manager.run()