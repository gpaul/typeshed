# Stubs for gettext (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class NullTranslations:
    def __init__(self, fp=None) -> None: ...
    def add_fallback(self, fallback): ...
    def gettext(self, message): ...
    def lgettext(self, message): ...
    def ngettext(self, msgid1, msgid2, n): ...
    def lngettext(self, msgid1, msgid2, n): ...
    def info(self): ...
    def charset(self): ...
    def output_charset(self): ...
    def set_output_charset(self, charset): ...
    def install(self, names=None): ...

class GNUTranslations(NullTranslations):
    LE_MAGIC = ...  # type: Any
    BE_MAGIC = ...  # type: Any
    def lgettext(self, message): ...
    def lngettext(self, msgid1, msgid2, n): ...
    def gettext(self, message): ...
    def ngettext(self, msgid1, msgid2, n): ...

def find(domain, localedir=None, languages=None, all=False): ...
def translation(domain, localedir=None, languages=None, class_=None, fallback=False,
                codeset=None): ...
def install(domain, localedir=None, codeset=None, names=None): ...
def textdomain(domain=None): ...
def bindtextdomain(domain, localedir=None): ...
def dgettext(domain, message): ...
def dngettext(domain, msgid1, msgid2, n): ...
def gettext(message): ...
def ngettext(msgid1, msgid2, n): ...

Catalog = ...  # type: Any