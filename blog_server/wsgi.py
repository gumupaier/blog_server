from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
import os
import logging
from dotenv import load_dotenv
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from blog_server import create_app  # noqa


def product():
    app = create_app('production')
    ip = "0.0.0.0"
    port = 5000
    logger.info("*"*88)
    logger.info("runing on {ip}:{port} ".format(ip=ip, port=port))
    server = WSGIServer((ip, port), app)
    server.serve_forever()


def main():
    product()

# main()
