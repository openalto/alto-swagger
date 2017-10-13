import connexion
from unicorn_server.models.error import Error
from unicorn_server.models.path_query_response import PathQueryResponse
from unicorn_server.models.query_desc import QueryDesc
from unicorn_server.models.resource_query_response import ResourceQueryResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


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
    return 'do some magic!'


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
    return 'do some magic!'
