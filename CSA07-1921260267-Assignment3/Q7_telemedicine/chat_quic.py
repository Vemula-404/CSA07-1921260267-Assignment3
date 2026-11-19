# Requires: pip install aioquic
# Minimal QUIC echo (client + server) — see repo README for full run
import asyncio
from aioquic.asyncio import serve, connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived


class Echo(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            self._quic.send_stream_data(event.stream_id, b"echo:" + event.data)


async def main():
    cfg = QuicConfiguration(is_client=False, alpn_protocols=["chat"])
    cfg.load_cert_chain("cert.pem", "key.pem")
    await serve("127.0.0.1", 4433, configuration=cfg, create_protocol=Echo)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())