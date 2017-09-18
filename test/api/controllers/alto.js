var should = require('should');
var request = require('supertest');
var server = require('../../../app');

describe('controllers', function() {

  describe('alto', function() {

    describe('GET /networkmap/default', function() {

      it('should return a default networkmap', function(done) {

        request(server)
          .get('/networkmap/default')
          .expect('Content-Type', 'application/alto-networkmap+json')
          .expect(200)
          .end(function(err, res) {
            should.not.exist(err);

            res.body.should.eql(
              require('../../../api/examples/networkmap-response-example.json'));

            done();
          });
      });

    });

    describe('POST /networkmap/default', function() {

      it('should return a filtered default networkmap', function(done) {

        request(server)
          .post('/networkmap/default')
          .send(require('../../../api/examples/networkmap-request-example.json'))
          .set('Content-Type', 'application/alto-networkmapfilter+json')
          .expect('Content-Type', 'application/alto-networkmap+json')
          .expect(200)
          .end(function(err, res) {
            should.not.exist(err);

            // res.body.should.eql('')

            done();
          });
      });

    });

  });

});
