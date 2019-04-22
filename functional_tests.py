# from https://www.obeythetestinggoat.com/book/chapter_01.html

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
