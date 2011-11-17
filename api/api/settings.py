# Scrapy settings for api project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'api'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['api.spiders']
NEWSPIDER_MODULE = 'api.spiders'
DEFAULT_ITEM_CLASS = 'api.items.ApiItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

