'use strict';

module.exports = {
  queryPath: queryPath,
  queryResource: queryResource
};

function queryPath(req, res) {
  if (req.method === 'POST') {
    var flows = req.swagger.params.flows.value
    var rib = require('../../config/rib')
    var nexthops = []
    flows.forEach(function (flow) {
      var nexthop = rib['bgp-rib'].find(function (e) {
        return (
          e.ingress == flow.ingress &&
          e.dest == flow.dest
        )
      }).next
      nexthops.push(nexthop)
    })
    res.json(nexthops)
    return
  }
}

function queryResource(req, res) {
  if (req.method === 'POST') {
    var flows = req.swagger.params.flows.value
    // Resource State Abstraction Query
    var topo = getTopology()
    var pv = getPathVector(flows)
    var rsa = generateRSA(topo, pv)
    res.json(rsa)
    return
  }
}

function getTopology() {
  var topo = {}
  // Retrieve topology from the SDN controller
  return topo
}

function getPathVector(flows) {
  var pv = []
  // Lookup Routing for flows
  return pv
}

function generateRSA(topo, pv) {
  var rsa = []
  // Calculate minimal equivalent constraints from topo and pv
  return rsa
}
