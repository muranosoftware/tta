from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
from itertools import islice
import six
from git import Repo


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    if isinstance(iterable, list) or isinstance(iterable, tuple):
        return iterable[:n]
    return list(islice(iterable, n))


@six.add_metaclass(ABCMeta)
class MonthWork(object):

    def __init__(self, email, patch=None):
        self.email = email
        self.patch = patch

    @abstractmethod
    def get_commits(self):
        pass

    def get_last_n_commits(self, n=25):
        commits = list(take(n, self.get_commits()))
        return reversed(commits)


class GitMonthWork(MonthWork):

    def filter_by_email(self, commit):
        return commit.author.email == self.email

    def get_message(self, commit):
        return commit.message.split('\n')[0]

    def get_commits(self):
        repo = Repo(self.patch)
        return map(self.get_message, filter(self.filter_by_email, repo.iter_commits()))