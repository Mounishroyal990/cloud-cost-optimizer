from app import create_app
from config import Config

app = create_app()

if __name__ == "__main__":
    print(f"Starting App on: http://{Config.FLASK_HOST}:{Config.FLASK_PORT}")
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=Config.DEBUG)
