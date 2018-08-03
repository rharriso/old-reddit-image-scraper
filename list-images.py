from selenium import webdriver
import re

driver = webdriver.Firefox()
# driver.get("https://old.reddit.com/r/spaceporn/search?q=nebula&sort=new&restrict_sr=on")
driver.get("https://old.reddit.com/r/spaceporn")
all_urls = []
pages = 1000


for _ in range(pages):
  # links = driver.find_elements_by_css_selector(".search-link")
  for button in driver.find_elements_by_css_selector(".expando-button"):
    button.click()

  links = driver.find_elements_by_css_selector(".media-preview-content .may-blank")
  urls = [link.get_attribute("href") for link in links
    if re.match(r".*\.(jpg)|(jpeg)|(png)$", link.get_attribute("href"))
  ]
  all_urls += urls

  # next page
  try:
    driver.find_element_by_css_selector("a[rel='nofollow next'").click()
  except:
    break

for i, url in enumerate(all_urls):
  print(url)
# try:
#   os.mkdir("/media/rharriso/Drobo7/Ross/Data/space-images")
# except:
#   pass

# k
# for i, url in enumerate(all_urls):
#   print(i, "of", len(all_urls))
#   wget.download(url, out="images")

