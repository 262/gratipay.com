"""
This module contains exceptions shared across application code.
"""

from __future__ import print_function, unicode_literals



class UnknownPlatform(Exception): pass

class ProblemChangingUsername(Exception):
    def __str__(self):
        return self.msg.format(self.args[0])

class UsernameIsEmpty(ProblemChangingUsername):
    msg = "You need to provide a username!"

class UsernameTooLong(ProblemChangingUsername):
    msg = "The username '{}' is too long."

# Not passing the potentially unicode characters back because of:
# https://github.com/gittip/aspen-python/issues/177
class UsernameContainsInvalidCharacters(ProblemChangingUsername):
    msg = "That username contains invalid characters."

class UsernameIsRestricted(ProblemChangingUsername):
    msg = "The username '{}' is restricted."

class UsernameAlreadyTaken(ProblemChangingUsername):
    msg = "The username '{}' is already taken."

class TooGreedy(Exception): pass
class NoSelfTipping(Exception): pass
class BadAmount(Exception): pass
