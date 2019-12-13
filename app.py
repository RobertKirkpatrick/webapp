from app import app
from app.models import User

#create shell context to initialize the database
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'twofact': twofac}