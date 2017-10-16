'''
configurations of SDN controllers
'''

UNICORN_LINK_SRC = 'link-src'
UNICORN_LINK_DST = 'link-dst'
UNICORN_LINK_WEIGHT = 'weight'

KYTOS_API_SERVER = 'http://127.0.0.1:8181'
KYTOS_TOPO_API_PATH = '/api/legacy/of_topology/topology'
KYTOS_KEY_LINKS = 'links'
KYTOS_TYPE = 'type'
KYTOS_LINK = 'link'
KYTOS_LINK_SRC = 'source'
KYTOS_LINK_DST = 'target'



'''DEBUG USE'''
routes = [[{'link-dst': '00:00:00:00:00:01', 
            'link-src': '00:00:00:00:00:00:00:01:1',
            'weight': 1},
           {'link-dst': '00:00:00:00:00:00:00:01:2',
            'link-src': '00:00:00:00:00:00:00:02:2',
            'weight': 1},
           {'link-dst': '00:00:00:00:00:00:00:02:1', 
            'link-src': '00:00:00:00:00:02',
            'weight': 1}
          ], 
          [{'link-dst': '00:00:00:00:00:01', 
            'link-src': '00:00:00:00:00:00:00:01:1',
            'weight': 1},
           {'link-dst': '00:00:00:00:00:00:00:01:2',
            'link-src': '00:00:00:00:00:00:00:02:2',
            'weight': 1},
          ], 
          [{'link-dst': '00:00:00:00:00:01', 
            'link-src': '00:00:00:00:00:00:00:01:1',
            'weight': 1},
           {'link-dst': '00:00:00:00:00:00:00:01:2',
            'link-src': '00:00:00:00:00:00:00:02:2',
            'weight': 1},
           {'link-dst': '00:00:00:00:00:00:00:02:1', 
            'link-src': '00:00:00:00:00:02',
            'weight': 1}
          ]
         ]
turn = 1







