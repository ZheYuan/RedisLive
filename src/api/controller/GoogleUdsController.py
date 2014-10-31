from BaseController import BaseController
import tornado.ioloop
import tornado.web

__author__ = 'zhe'

class GoogleUdsController(BaseController):

    def get(self):
        module = self.get_argument("file")
        version = self.get_argument("v")
        packages = self.get_argument("packages")

        file_name = module + '_' + version + '_' + packages + ".js"
        self.redirect(file_name);

        file_object = open(file_name)
        try:
             return_text = file_object.read()
        finally:
            file_object.close()

        self.write(return_text)