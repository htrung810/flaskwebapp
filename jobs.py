import requests
import sqlite3
from flask import Blueprint, render_template

jobs = Blueprint("jobs",__name__)
conn = sqlite3.connect('database.db', check_same_thread= False)
c = conn.cursor()
try:
    c.execute('CREATE TABLE jobs(title, link)')
except Exception:
    pass
r = requests.get("https://api.github.com/repos/awesome-jobs/vietnam/issues").json()


@jobs.route('/listblog/laptrinh/programming/')
def get_job():
    list_job = []
    for add_job in r:
        titl = add_job['title']
        link_job = add_job['html_url']
        if c.execute(f"SELECT link FROM jobs WHERE link = '{link_job}'").fetchone() is None:
            list_job.append((titl, link_job))
    c.executemany("INSERT INTO jobs VALUES(?, ?)", list_job)
    c.execute('SELECT * FROM jobs')
    return render_template('programming.html', rows = c.fetchall())
