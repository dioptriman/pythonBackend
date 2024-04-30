import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is a python command!")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animal", listRequestHandler),
        (r"/isEven", queryParamRequestHandler)
    ])

    port = 8882
    app.listen(8882)
    print(f"Application is listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
