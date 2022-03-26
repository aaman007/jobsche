from multiprocessing import cpu_count
from dotenv import load_dotenv


def max_workers():
    return cpu_count() * 2 + 1


load_dotenv()

bind = '0.0.0.0:5000'
max_requests = 1000
workers = max_workers()
wsgi_app = 'jobsche.server:app'
