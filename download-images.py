from selenium import webdriver
import re
import wget

driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/spaceporn/search?q=nebula&sort=new&restrict_sr=on")
all_urls = []
pages = 2


for _ in range(pages):
  links = driver.find_elements_by_css_selector(".search-link")
  urls = [link.get_attribute("href") for link in links
    if re.match(r".*\.(jpg)|(jpeg)|(png)$", link.get_attribute("href"))
  ]
  all_urls += urls

  # next page
  driver.find_element_by_css_selector("a[rel='nofollow next'").click()

for url in all_urls:
  wget.download(url)

