import multiprocessing

bind = '127.0.0.1:2552'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
accesslog = '/srv/jungle/log/gunicorn_access'
errorlog = '/srv/jungle/log/gunicorn_error'
loglevel = 'error'
pythonpath = '/srv/jungle/www/jungle'
user = 'volterra'
group = 'volterra'
