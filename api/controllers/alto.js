'use strict';

module.exports = {
  networkmap: networkmap,
  costmap: costmap,
  endpointcost: endpointcost,
  endpointprop: endpointprop,
  directory: directory
};

var SAMPLE_ERROR_RESPONSE = {
  meta: {
    code: 'E_MISSING_FIELD',
    description: 'A required JSON field is missing',
    message: 'Unknown error'
  }
}

function networkmap(req, res) {
  var resourceId = req.swagger.params.resourceId.value
  if (req.method === 'GET') {
    if (getFullNetworkMap(req.swagger.params.resourceId.value, res)) {
      return
    }
  } else if (req.method === 'POST') {
    if (getFilteredNetworkMap(req.swagger.params.resourceId.value,
      req.swagger.params.filter.value, res)) {
      return
    }
  }

  // if (resourceId === 'default') {
  //   var data = require('../examples/networkmap-response-example.json')
  //   if (req.method === 'GET') {
  //     res.json(data)
  //     return
  //   } else if (req.method === 'POST') {
  //     var filter = req.swagger.params.filter.value
  //     res.json({
  //       meta: data.meta,
  //       'network-map': filteredNetworkmap(data['network-map'], filter)
  //     })
  //     return
  //   }
  // }

  res.json(SAMPLE_ERROR_RESPONSE)
}

function getFullNetworkMap(resourceId, res) {
  if (resourceId === 'default') {
    res.json(require('../examples/networkmap-response-example.json'))
    return true
  }
  return false
}

function getFilteredNetworkMap(resourceId, filter, res) {
  if (resourceId === 'default') {
    res.json({
      meta: data.meta,
      'network-map': filteredNetworkmap(data['network-map'], filter)
    })
    return true
  }
  return false
}

function filteredNetworkmap(data, filter) {
  var filteredData = {}
  filter.pids.forEach(function(pid) {
    if (data[pid]) {
      var pidData = {}
      if (filter['address-types'] && filter['address-types'].length) {
        filter['address-types'].forEach(function(addressType) {
          if (data[pid][addressType]) {
            pidData[addressType] = data[pid][addressType]
          }
        })
      } else {
        pidData = data[pid]
      }
      if (Object.keys(pidData)) {
        filteredData[pid] = pidData
      }
    }
  })
  return filteredData
}

function costmap(req, res) {
  if (req.method === 'GET') {
    // TODO: Retrieve costmap
  } else if (req.method === 'POST') {
    // TODO: Retrieve costmap by filter
  }
  res.json(SAMPLE_ERROR_RESPONSE)
}

function endpointcost(req, res) {
  if (req.method === 'POST') {
    // TODO: Lookup endpoint cost service
  }
  res.json(SAMPLE_ERROR_RESPONSE)
}

function endpointprop(req, res) {
  // TODO: Lookup endpoint property service
  res.json(SAMPLE_ERROR_RESPONSE)
}

function directory(req, res) {
  // TODO: Retrieve the information resource directory
  res.json(SAMPLE_ERROR_RESPONSE)
}
