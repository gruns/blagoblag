import datetime
import os

from liquidluck.options import settings, g
from liquidluck.readers.base import Post
from liquidluck.readers.restructuredtext import RestructuredTextReader
from liquidluck.writers import core
from liquidluck.writers.base import get_post_slug


class DateFromPathPost(Post):
    MONTHS_BY_NAME = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }

    @property
    def date(self):
        if "blog" not in self.filepath:
            # Posts don't have a date
            return None
        _, _, year, month_name, day, _ = self.filepath.split("/", 6)
        month = self.MONTHS_BY_NAME[month_name]
        return datetime.date(int(year), int(month), int(day))

    @property
    def month_name(self):
        return self.date.strftime("%b").lower()


class DateFromPathRestructuredTextReader(RestructuredTextReader):
    post_class = DateFromPathPost


def get_post_destination(post, slug_format):
    slug = get_post_slug(post, slug_format)

    if slug.endswith('.html'):
        return slug
    elif slug.endswith("/"):
        return slug + 'index.html'
    else:
        return slug + '.html'


class DirectoryPostWriter(core.PostWriter):
    def _dest_of(self, post):
        dest = get_post_destination(post, settings.config['permalink'])
        return os.path.join(g.output_directory, dest)


class DirectoryPageWriter(core.PageWriter):
    def start(self):
        l = len(g.source_directory) + 1
        for post in g.pure_pages:
            template = post.template or self._template
            filename = os.path.splitext(post.filepath[l:])[0] + '/index.html'
            dest = os.path.join(g.output_directory, filename)
            self.render({'post': post}, template, dest)
