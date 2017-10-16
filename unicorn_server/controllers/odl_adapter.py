import requests
from urllib3.exceptions import ConnectionError
from unicorn_server.controllers.mock_adapter import Adapter


class ODLAdapter(Adapter):
    """
    Create a reverse proxy to adapt Unicorn APIs in OpenDaylight.
    """

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
            return Error(meta=ErrorMeta(code='E_UNKNOWN', message=str(e))), 500
        if response.status_code // 100 != 2:
            return response.reason
        else:
            return response.json()['output']

    def get_resource(self, query_set=[]):
        try:
            response = self.restconf('/operations/pathmanager:query-resource',
                                     data={'input': query_set})
        except requests.exceptions.RequestException as e:
            return Error(meta=ErrorMeta(code='E_UNKNOWN', message=str(e))), 500
        if response.status_code // 100 != 2:
            return response.reason
        else:
            return response.json()['output']
