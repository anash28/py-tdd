from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#blah blah blah
assert 'Django' in browser.title
