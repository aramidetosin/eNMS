from socketserver import BaseRequestHandler, UDPServer
from threading import Thread

from eNMS.database import Session
from eNMS.database.functions import fetch, factory, fetch_all


class SyslogServer:
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.start()

    def start(self) -> None:
        UDPServer.allow_reuse_address = True
        self.server = UDPServer((self.ip_address, self.port), SyslogUDPHandler)
        th = Thread(target=self.server.serve_forever)
        th.daemon = True
        th.start()


class SyslogUDPHandler(BaseRequestHandler):
    def handle(self) -> None:
        address = self.client_address[0]
        device = fetch("Device", allow_none=True, ip_address=address)
        properties = {
            "source": device.name if device else address,
            "content": str(bytes.decode(self.request[0].strip())),
        }
        for event in fetch_all("Event"):
            event.match_log(**properties)
        log = factory("Syslog", **properties)
        Session.add(log)
        Session.commit()