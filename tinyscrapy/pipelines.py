# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from misc.store import doubanDB

class DmozPipeline(object):
    def process_item(self, item, spider):
        spec = { "title": item["title"] }
        doubanDB.dmoz.update(spec, {'$set': dict(item)}, upsert=True)
        return None

class MoviePipeline(object):
    def process_item(self, item, spider):
        if spider.name != "movie":  return item
        if item.get("subject_id", None) is None: return item

        spec = { "subject_id": item["subject_id"] }
        doubanDB.movie.update(spec, {'$set': dict(item)}, upsert=True)

        return None
