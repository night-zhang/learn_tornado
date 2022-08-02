import asyncio
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    # py3.6
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())

    # py>3.6
    # asyncio.run(main())
