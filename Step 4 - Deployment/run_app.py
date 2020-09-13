from src.utils.config import get_default
from src.template_app import app
import logging

HOST = get_default('flask_app', 'host')
PORT = get_default('flask_app', 'port')

logging.basicConfig(filename=get_default('logger', 'filename'), 
                    level=get_default('logger', 'level'), 
                    format=get_default('logger', 'format'))

app.run(host=HOST,
        port=int(PORT),
        debug=True,
        use_reloader=False)
