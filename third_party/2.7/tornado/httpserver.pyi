# Stubs for tornado.httpserver (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from tornado import httputil
from tornado.tcpserver import TCPServer
from tornado.util import Configurable

class HTTPServer(TCPServer, Configurable, httputil.HTTPServerConnectionDelegate):
    def __init__(self, *args, **kwargs) -> None: ...
    request_callback = ... # type: Any
    no_keep_alive = ... # type: Any
    xheaders = ... # type: Any
    protocol = ... # type: Any
    conn_params = ... # type: Any
    def initialize(self, request_callback, no_keep_alive=False, io_loop=None, xheaders=False, ssl_options=None, protocol=None, decompress_request=False, chunk_size=None, max_header_size=None, idle_connection_timeout=None, body_timeout=None, max_body_size=None, max_buffer_size=None): ...
    @classmethod
    def configurable_base(cls): ...
    @classmethod
    def configurable_default(cls): ...
    def close_all_connections(self): ...
    def handle_stream(self, stream, address): ...
    def start_request(self, server_conn, request_conn): ...
    def on_close(self, server_conn): ...

class _HTTPRequestContext:
    address = ... # type: Any
    protocol = ... # type: Any
    address_family = ... # type: Any
    remote_ip = ... # type: Any
    def __init__(self, stream, address, protocol) -> None: ...

class _ServerRequestAdapter(httputil.HTTPMessageDelegate):
    server = ... # type: Any
    connection = ... # type: Any
    request = ... # type: Any
    delegate = ... # type: Any
    def __init__(self, server, server_conn, request_conn) -> None: ...
    def headers_received(self, start_line, headers): ...
    def data_received(self, chunk): ...
    def finish(self): ...
    def on_connection_close(self): ...

HTTPRequest = ... # type: Any