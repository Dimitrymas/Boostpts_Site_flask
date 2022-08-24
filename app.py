from routers.index_router import index_routers
from sweater import app

index_routers(app)

if __name__ == "__main__":
    app.run(host='192.168.0.106', port=80, debug=True)
