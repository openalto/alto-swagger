import os
import connexion
from unicorn_server.models.query_desc import QueryDesc
from unicorn_server.controllers.mock_adapter import Adapter, __Adapter
from unicorn_server.controllers.odl_adapter import ODLAdapter
from unicorn_server.controllers.kytos_adapter import KytosAdapter

# basedir = os.path.join(os.path.dirname(__file__), '..')

class UnknownBackendError(Exception):
    """Unknown backend error."""

class AdapterTalker:
    """
    Factory class for backend adapter.
    """
    @classmethod
    def set_backend_adapter(cls, backend='mock', url='http://localhost:8181',
                            auth=None, settings=None):
        global __Adapter
        if 'mock' == backend:
            __Adapter = Adapter(url, auth)
        elif 'odl' == backend:
            __Adapter = ODLAdapter(url, auth)
        elif 'kytos' == backend:
            __Adapter = KytosAdapter(url, auth)
        else:
            raise UnknownBackendError('Unknown backend type is set.')

def query_path(query_set):
    """
    query_path
    Make a recursive path query
    :param query_set:
    :type query_set: list | bytes

    :rtype: PathQueryResponse
    """
    global __Adapter
    if connexion.request.is_json:
        query_set = [QueryDesc.from_dict(d) for d in connexion.request.get_json()]
    return __Adapter.controller.get_as_path(query_set)


def query_resource(query_set):
    """
    query_resource
    Returns resource state abstraction in simple mode
    :param query_set:
    :type query_set: list | bytes

    :rtype: ResourceQueryResponse
    """
    global __Adapter
    if connexion.request.is_json:
        query_set = [QueryDesc.from_dict(d) for d in connexion.request.get_json()]
    return __Adapter.controller.get_resource(query_set)
