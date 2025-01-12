# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.io/en/latest/deploy.html
import deploy

from books import settings
from books.spiders import books

[settings]
default = books.settings

[deploy]
#url = http://localhost:6800/
project = books
