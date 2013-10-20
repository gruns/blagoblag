import datetime

from liquidluck.readers.base import Post
from liquidluck.readers.restructuredtext import RestructuredTextReader


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
