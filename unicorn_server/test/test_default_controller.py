# coding: utf-8

from __future__ import absolute_import

from unicorn_server.models.query_desc import QueryDesc
from unicorn_server.models.flow_spec import FlowSpec
from . import BaseTestCase
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_query_path(self):
        """
        Test case for query_path


        """
        query_set = [QueryDesc(flow=FlowSpec(src_ip='192.168.1.100',
                                             dst_ip='192.168.2.100',
                                             dst_port=54321,
                                             protocol='tcp'),
                               ingress_point=''),
                     QueryDesc(flow=FlowSpec(src_ip='192.168.2.101',
                                             dst_ip='192.168.3.101',
                                             dst_port=8080,
                                             protocol='tcp'),
                               ingress_point='172.17.0.2')]
        response = self.client.open('/v1/unicorn/ext/query/path',
                                    method='POST',
                                    data=json.dumps(query_set),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_query_resource(self):
        """
        Test case for query_resource


        """
        query_set = [QueryDesc(flow=FlowSpec(src_ip='192.168.2.101',
                                             dst_ip='192.168.3.101',
                                             dst_port=8080,
                                             protocol='tcp'),
                               ingress_point='172.17.0.2')]
        response = self.client.open('/v1/unicorn/ext/query/resource',
                                    method='POST',
                                    data=json.dumps(query_set),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
