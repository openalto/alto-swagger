#!/usr/bin/env python3

import argparse
import connexion
from .encoder import JSONEncoder
from .controllers.default_controller import AdapterTalker

adapter = {
    'mock': 'default_controller',
    'odl': 'odl_adapter',
    'kytos': 'kytos_adapter'
}

def parse_argument():
    parser = argparse.ArgumentParser(description='Unicorn Domain Manager.')
    parser.add_argument('-B', '--backend', dest='backend', default='mock',
                        type=str, choices=adapter.keys(),
                        help='set backend controller.')
    parser.add_argument('-a', '--addr', dest='address',
                        default='localhost', type=str,
                        help='ip address of the backend controller (default: localhost).')
    parser.add_argument('-p', '--port', dest='port',
                        default='8181', type=int,
                        help='tcp port the backend controller REST API will listen on (default: 8181).')
    parser.add_argument('-A', '--auth', dest='auth',
                        default='', type=str,
                        help='the authentication of the backend controller REST API.')
    parser.add_argument('-s', '--secure', dest='secure', action='store_true',
                        help='use HTTPS to talk to REST API of the backend controller.')
    args = parser.parse_args()
    return args

def setup_controller(args):
    url = 'http'
    if args.secure:
        url += 's'
    url += '://' + args.address + ':' + str(args.port)
    auth = None
    if args.auth:
        auth = tuple(args.auth.split(':'))

    return AdapterTalker.set_backend_adapter(args.backend, url, auth)

if __name__ == '__main__':
    args = parse_argument()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    # print(__Adapter.controller.url, __Adapter.controller.auth, __Adapter.controller.get_as_path)
    setup_controller(args)
    # print(__Adapter.controller.url, __Adapter.controller.auth, __Adapter.controller.get_as_path)
    app.add_api('swagger.yaml', arguments={'controller': 'default_controller'})
    app.run(port=9000, threaded=True)
