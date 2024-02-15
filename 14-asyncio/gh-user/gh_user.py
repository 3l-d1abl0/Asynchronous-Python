"""Getting user information from GitHub"""

from urllib.request import urlopen
from collections import namedtuple
from datetime import datetime
import json

User = namedtuple('User', 'login name joined')


def user_info(login):
    """Get user information from GitHub"""
    url = 'https://api.github.com/users/{}'.format(login)
    fp = urlopen(url)
    reply = json.load(fp)

    joined = datetime.strptime(reply['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    return User(login, reply['name'], joined)
    


def users_info(logins):
    """Get users information from GitHub"""
    return [user_info(login) for login in logins]


if __name__ == '__main__':
    logins = [
        'gvanrossum',
        'wesm',
        'tebeka',
        'torvalds',
        '3l-d1abl0',
    ]

    print(users_info(logins))