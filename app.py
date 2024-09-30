from flask import Flask
from config import SERVER_HOST, SERVER_PORT, DEBUG
from presentation import user_blueprint, group_blueprint, transaction_blueprint
from infrastructure.repositories import Repositories

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(group_blueprint, url_prefix="/group")
app.register_blueprint(transaction_blueprint, url_prefix="/transaction")

Repositories.init_tables()

if __name__ == "__main__":
    app.run(debug=DEBUG, host=SERVER_HOST, port=SERVER_PORT)