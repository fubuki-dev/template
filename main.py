from fubuki import Fubuki
from app.routes import setup_routes

app = Fubuki()
setup_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)