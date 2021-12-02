# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector


class CrawlingPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'people'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS links_tb""")
        self.curr.execute("""create table links_tb(
            link longtext,
            content longtext
        )""")

    def process_item(self, item, spider):
        print("Link: " + item['link'])
        print("Content: " + item['content'])
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into links_tb values (%s, %s)""", (
            item['link'],
            item['content']
        ))
        self.conn.commit()
