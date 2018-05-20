import os
from api.response import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 7777))
    app.run(host=host, port=port)