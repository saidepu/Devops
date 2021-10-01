import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)
browser.open(base_url)
form = browser.get_form(action='/login/')

form["username"] = ''
form["password"] = ''
browser.session.headers['Referer'] = ''

browser.submit_form(form)
print(str(browser.select))
