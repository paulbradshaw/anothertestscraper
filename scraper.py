# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

print("hello")
#
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
# Show what's in the variable html
print(html)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")
print(root)
footers = root.cssselect("div#footer")
print(footers)
for footer in footers:
  footertextall = footer.text_content()
  print(len(footertextall))
  print(footertextall[1:5])
  print(footer)
  convertedfooter = lxml.html.tostring(footer)
  print(convertedfooter)
  footertext = footer.text
  print(footertext)
  print(footer.attrib['id'])
  #print(footertextall)
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
