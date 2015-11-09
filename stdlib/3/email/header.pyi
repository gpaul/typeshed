# Stubs for email.header (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

def decode_header(header): ...
def make_header(decoded_seq, maxlinelen=None, header_name=None, continuation_ws=''): ...

class Header:
    def __init__(self, s=None, charset=None, maxlinelen=None, header_name=None,
                 continuation_ws='', errors=''): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def append(self, s, charset=None, errors=''): ...
    def encode(self, splitchars='', maxlinelen=None, linesep=''): ...

class _ValueFormatter:
    def __init__(self, headerlen, maxlen, continuation_ws, splitchars) -> None: ...
    def newline(self): ...
    def add_transition(self): ...
    def feed(self, fws, string, charset): ...

class _Accumulator(list):
    def __init__(self, initial_size=0) -> None: ...
    def push(self, fws, string): ...
    def pop_from(self, i=0): ...
    def __len__(self): ...
    def reset(self, startval=None): ...
    def is_onlyws(self): ...
    def part_count(self): ...