from nats import connect
import asyncio
import logging


def main():
    logging.info('service started')
    asyncio.run(init_nats())


async def msg_handler(msg):
    logging.info('Message: %s', msg.subject)


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
