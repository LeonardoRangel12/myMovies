import os
from multiprocessing import Pool
processes  = ('manage.py runserver','./tailwindcss -i static/src/input.css -o static/output.css --watch')
def run_process(process):
    os.system('python {}'.format(process))

pool = Pool(processes=2)
pool.map(run_process, processes)
