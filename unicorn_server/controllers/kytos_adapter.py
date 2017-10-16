import connexion
import json
import numpy as np
import os
import requests

from pprint import pprint
from unicorn_server.models.query_desc import QueryDesc
from unicorn_server import settings

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
        #log.info(query_set[0])
        #log.info(len(query_set))

        """
        open the egress2ingress mapping file
        """
        with open(os.path.dirname(__file__) + '/../egress2ingress-config.json') as data_file:
            egress2ingress = json.load(data_file)
        pprint(egress2ingress)

        next_ingress_array = []

        for query in query_set:

            """
            get the egress point of each flow, depending on the routing system
            """
            egress = get_egress_point(query)

            """
            get the next ingress point of each flow from pre-configured e2i mapping
            """
            next_ingress_array.append(egress2ingress[egress[0]][egress[1]])
        return next_ingress_array
    else:
        """TODO: this part seems redundant?"""
        code = 'E_SYNTAX'
        message = 'The input does not follow the JSON format'
        meta = {{'code': code, 'message': message}}
        return json.dumps(meta)

    #return 'implement kytos adapter here!'


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
        all_links = get_links_kytos()
        A = np.zeros((len(all_links), len(query_set)))
        C = np.zeros((len(all_links), 1))

        
        '''
        for each flow, query routing system to get all used links and update A
        '''
        for query_idx, query in enumerate(query_set):
            used_links = get_links_from_route(query)
            for link in used_links:
                for idx, value in enumerate(all_links):
                    if value[settings.UNICORN_LINK_SRC] == link[settings.UNICORN_LINK_SRC] \
                       and value[settings.UNICORN_LINK_DST] == link[settings.UNICORN_LINK_DST]:
                        A[idx][query_idx] = link[settings.UNICORN_LINK_WEIGHT]
#        pprint(A)

        '''
        for each link, if it is used by at least one flow, get its available bandwidth
        '''
        for idx in range(C.shape[0]):
            if np.count_nonzero(A[idx, :]) > 0:
                C[idx] = get_availbw(all_links[idx])
#        pprint(C)
               
        '''
        assemble the original A X \leq C matrix by removing unused links
        '''
        A = A[~np.all(A == 0, axis=1)]
        C = C[~np.all(C == 0, axis=1)]
#        pprint(A)
#        pprint(C)

        '''
        run MECS to compute A' X \leq C'
        '''
        (A_mecs, C_mecs) = MECS(A, C)
        pprint(A_mecs)
        pprint(C_mecs)
        '''
        return A' and C'
        '''
        ane_matrix = []
        anes = []
        for ane_idx in range(A.shape[0]):
            ane_flow_coefficient = []
            anes.append({'availbw': C[ane_idx][0]})
            for flow_idx in range(A.shape[1]):
                if A[ane_idx][flow_idx] != 0:
                    ane_flow_coefficient.append({'coefficient': A[ane_idx][flow_idx], 'flowid': flow_idx})
            ane_matrix.append(ane_flow_coefficient)
        resource_state_abstraction = {'ane-matrix': ane_matrix, 'anes': anes}
        #return json.dumps(resource_state_abstraction)
        return resource_state_abstraction
    #return 'implement kytos adapter here!'


def get_links_kytos():
    '''get all the links in the network'''
    topology = requests.get(settings.KYTOS_API_SERVER+settings.KYTOS_TOPO_API_PATH)
    topology_json = json.loads(topology.text)
    links = [{settings.UNICORN_LINK_SRC: link[settings.KYTOS_LINK_SRC],
              settings.UNICORN_LINK_DST: link[settings.KYTOS_LINK_DST]} 
              for link in topology_json[settings.KYTOS_KEY_LINKS] 
                      if link[settings.KYTOS_TYPE] == settings.KYTOS_LINK]        
    return (links)

def get_egress_point(query):
    """TODO: depend on the routing system imlementation"""
    return ('192.151.1.102', '2')

def get_links_from_route(query):
    '''TODO: depend on the routing system implementation'''
    settings.turn = (settings.turn + 1) % 2
    return settings.routes[settings.turn]

def get_availbw(link):
    '''return the index of of a given link in the list of links'''
    '''TODO: depend on the stats system implementation'''
    pprint(link)
    return 1000000

def MECS(A, C):
    '''TODO: run the MECS algorithm to compute the minimal, equivalent resource state abstraction'''
    A_mesc = A
    C_mesc = C
    return (A_mesc, C_mesc)





