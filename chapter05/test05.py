import pymysql

conn = pymysql.connect(host = 'nicekkong.com',
                       user='scraping',
                       passwd='scraping!@',
                       db='scrapingdev'
                       )

cur = conn.cursor()
# cur.execute("USE scrapingdev")
cur.execute("SELECT * FROM pages WHERE id=3")
print(cur.fetchone())
cur.close()
conn.close()

