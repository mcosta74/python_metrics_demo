from prometheus_client import start_http_server, Counter
from nats import connect
import asyncio
import logging

REQUEST_COUNTER = Counter(
    'messages_total',
    'number of messages received from NATS', 
    namespace='demo',
    labelnames=['subpath']
)


def main():
    logging.info('service started')
    start_http_server(8080)
    logging.info('metrics exposed at http://localhost:8080/metrics')

    print('Hello world')

    asyncio.run(init_nats())


async def msg_handler(msg):
    logging.info('Message: %s', msg.subject)

    tokens = msg.subject.split('.')
    subpath = tokens[1] if len(tokens) >= 2 else ''
    REQUEST_COUNTER.labels(subpath).inc()


async def init_nats():
    nc = await connect("demo.nats.io")

    await nc.subscribe('massimo.>', cb=msg_handler)
    logging.info('ready for new messages...')

    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        print('Bye')
