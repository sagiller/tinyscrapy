# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from misc.mysql_store import DmozItem
class peeweeDmozPipeline(object):
    def process_item(self, item, spider):
        item = DmozItem(title=item['title'], link=item['link'], desc=item['desc'])
        item.save()
