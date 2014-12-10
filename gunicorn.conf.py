import multiprocessing

bind = "127.0.0.1:2552"
workers = multiprocessing.cpu_count() * 2 + 1
