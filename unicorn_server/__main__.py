#!/usr/bin/env python3

import sys
import argparse
import connexion
from .encoder import JSONEncoder

adapter = {
    'mock': 'default_controller',
    'odl': 'odl_adapter',
    'kytos': 'kytos_adapter'
}

def parse_argument():
    parser = argparse.ArgumentParser(description='Unicorn Domain Manager.')
    parser.add_argument('-B', '--backend', dest='backend', default='mock',
                        type=str, choices=adapter.keys())
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_argument()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'controller': adapter[args.backend]})
    app.run(port=9000, threaded=True)
