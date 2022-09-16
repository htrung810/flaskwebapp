import requests, sqlite3
from flask import Blueprint, render_template
from bs4 import BeautifulSoup

conn = sqlite3.connect("database.db", check_same_thread= False)
c = conn.cursor()
familug = Blueprint("familug", __name__)


try:
    c.execute("CREATE TABLE python(name, link)")
    c.execute("CREATE TABLE command(name, link)")
    c.execute("CREATE TABLE sysadmin(name, link)")
    c.execute("CREATE TABLE latest(name, link)")
except Exception:
    pass


#famipython
@familug.route('/listblog/laptrinh/famipython/')
def fami_python():
    r = requests.get("https://www.familug.org/search/label/Python")
    tree = BeautifulSoup(markup= r.text, features="html.parser")
    post_name = tree.find_all(name= 'h3', attrs= {'class': 'post-title entry-title'})
    add_python = []
    for fami in post_name:
        fami_title = fami.contents[1].text
        fami_link = fami.contents[1].get('href')
        if c.execute(f"SELECT link FROM python WHERE link = '{fami_link}'").fetchone() is None:
            add_python.append((fami_title, fami_link))
    c.executemany("INSERT INTO python VALUES(?, ?)", add_python)
    conn.commit()
    c.execute('SELECT * FROM python')
    return render_template('famipython.html', rows = c.fetchall())


#fami command
@familug.route('/listblog/laptrinh/famicommand/')
def fami_command():
    r = requests.get("https://www.familug.org/search/label/Command")
    tree = BeautifulSoup(markup= r.text, features="html.parser")
    post_name = tree.find_all(name= 'h3', attrs= {'class': 'post-title entry-title'})
    add_command = []
    for fami in post_name:
        fami_title = fami.contents[1].text
        fami_link = fami.contents[1].get('href')
        if c.execute(f"SELECT link FROM command WHERE link = '{fami_link}'").fetchone() is None:
            add_command.append((fami_title, fami_link))
    c.executemany("INSERT INTO command VALUES(?, ?)", add_command)
    conn.commit()
    c.execute('SELECT * FROM command')
    return render_template('famicommand.html', rows = c.fetchall())


#fami sysadmin
@familug.route('/listblog/laptrinh/sysadmin/')
def fami_sysadmin():
    r = requests.get("https://www.familug.org/search/label/sysadmin")
    tree = BeautifulSoup(markup= r.text, features="html.parser")
    post_name = tree.find_all(name= 'h3', attrs= {'class': 'post-title entry-title'})
    add_sysadmin = []
    for fami in post_name:
        fami_title = fami.contents[1].text
        fami_link = fami.contents[1].get('href')
        if c.execute(f"SELECT link FROM sysadmin WHERE link = '{fami_link}'").fetchone() is None:
            add_sysadmin.append((fami_title, fami_link))
    c.executemany("INSERT INTO sysadmin VALUES(?, ?)", add_sysadmin)
    conn.commit()
    c.execute('SELECT * FROM sysadmin')
    return render_template('famisys.html', rows = c.fetchall())
