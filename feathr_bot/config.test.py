import pathlib

basedir = pathlib.Path(__file__).parent.resolve()

# db config
SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'feathr_bot_test.db'}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# openai
OPENAI_API_KEY = ""
