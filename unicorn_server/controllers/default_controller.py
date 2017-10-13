import os
import json
import connexion
from unicorn_server.models.query_desc import QueryDesc

basedir = os.path.join(os.path.dirname(__file__), '..')

def query_path(query_set):
    """
    query_path
    Make a recursive path query
    :param query_set:
    :type query_set: list | bytes

    :rtype: PathQueryResponse
    """
    if connexion.request.is_json:
        query_set = [QueryDesc.from_dict(d) for d in connexion.request.get_json()]
    # do some magic!
    return json.load(open(os.path.join(basedir, 'examples/query_path.response.json')))


def query_resource(query_set):
    """
    query_resource
    Returns resource state abstraction in simple mode
    :param query_set:
    :type query_set: list | bytes

    :rtype: ResourceQueryResponse
    """
    if connexion.request.is_json:
        query_set = [QueryDesc.from_dict(d) for d in connexion.request.get_json()]
    # do some magic!
    return json.load(open(os.path.join(basedir, 'examples/query_resource.response.json')))
