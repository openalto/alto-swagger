import requests
from urllib3.exceptions import ConnectionError
from unicorn_server.controllers.mock_adapter import Adapter


class ODLAdapter(Adapter):
    """
    Create a reverse proxy to adapt Unicorn APIs in OpenDaylight.
    """

    # def __init__(self, url='http://localhost:8181', auth=('admin', 'admin')):
    #     Adapter.__init__(self, url, auth)
    #     Adapter.controller.get_as_path = self.get_as_path
    #     Adapter.controller.get_resource = self.get_resource

    def restconf(self, node, data=None):
        headers = {'Content-type': 'application/json'}
        endpoint = self.controller.url + '/restconf' + node
        print(endpoint, headers, self.controller.auth)
        if data == None:
            response = requests.get(endpoint,
                                    headers=headers,
                                    auth=self.controller.auth)
        else:
            response = requests.post(endpoint,
                                     headers=headers,
                                     data=data,
                                     auth=self.controller.auth)
        return response

    def get_as_path(self, query_set=[]):
        try:
            response = self.restconf('/operations/pathmanager:query-path')
        except (requests.exceptions.RequestException, ConnectionError) as e:
            return {'code': str(e.errno),
                    'type': 'RequestException',
                    'value': str(e)}, 500
        if response.status_code // 100 != 2:
            return response.reason
        else:
            return response.json()

    def get_resource(self, query_set=[]):
        try:
            response = self.restconf('/operations/pathmanager:query-resource',
                                     data={'input': query_set})
        except requests.exceptions.RequestException as e:
            return {'code': str(e.errno),
                    'type': 'RequestException',
                    'value': str(e)}, 500
        if response.status_code // 100 != 2:
            return response.reason
        else:
            return response.json()


# def query_path(query_set):
#     """
#     query_path
#     Make a recursive path query
#     :param query_set:
#     :type query_set: list | bytes

#     :rtype: PathQueryResponse
#     """
#     print("post body is ready!")
#     if connexion.request.is_json:
#         print("post body is in json format!")
#         params = connexion.request.get_json()
#         print("read post body successfully!")
#         query_set = [QueryDesc.from_dict(d) for d in params]
#     return __Adapter.get_as_path(query_set)


# def query_resource(query_set):
#     """
#     query_resource
#     Returns resource state abstraction in simple mode
#     :param query_set:
#     :type query_set: list | bytes

#     :rtype: ResourceQueryResponse
#     """
#     if connexion.request.is_json:
#         query_set = [QueryDesc.from_dict(d) for d in connexion.request.get_json()]
#     return __Adapter.get_resource(query_set)
