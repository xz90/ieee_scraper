# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Container -> Pipeline -> SQL/Mongo database

import sqlite3

class QuotetutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("cs-professors.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                        name text,
                        title text,
                        email text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
            item['name'][0],
            item['title'][0],
            item['email'][0]
        ))
        self.conn.commit()
