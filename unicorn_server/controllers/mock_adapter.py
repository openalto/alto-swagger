import os
import json

basedir = os.path.join(os.path.dirname(__file__), '..')

class Adapter:
    """
    Reverse proxy to adapt Unicorn APIs in different backend controllers.
    """
    class __Controller:
        """
        Singleton instance of controller.
        """
        def __init__(self, url='http://localhost:8181', auth=None, settings=None):
            """Abstract init function"""
            self.url = url
            self.auth = auth
            self.settings = settings
            self.get_as_path = Adapter.get_as_path
            self.get_resource = Adapter.get_resource

    controller = None

    def __init__(self, url='http://localhost:8181', auth=None, settings=None):
        """Init function"""
        if not Adapter.controller:
            Adapter.controller = Adapter.__Controller(url, auth, settings)
        else:
            Adapter.controller.url = url
            Adapter.controller.auth = auth
            Adapter.controller.settings = settings
            Adapter.controller.get_as_path = self.get_as_path
            Adapter.controller.get_resource = self.get_resource

    def get_as_path(self, query_set=[]):
        """Implement adapter interface for path query"""
        return json.load(open(os.path.join(basedir, 'examples/query_path.response.json')))

    def get_resource(self, query_set=[]):
        """Implement adapter interface for resource query"""
        return json.load(open(os.path.join(basedir, 'examples/query_resource.response.json')))

__Adapter = Adapter()
