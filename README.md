# The OpenAPI specification for ALTO

> **NOTE:** Current specification is based on OpenAPI 2.0. We are planning to
> migrate the specification to OpenAPI 3.0 once the swagger 3.0.0 is released.

[![Travis status](https://img.shields.io/travis/openalto/alto-swagger/spec.svg)](https://travis-ci.org/openalto/alto-swagger)

- [api/alto.yaml](https://github.com/openalto/alto-swagger/raw/spec/api/alto.yaml) is
  the entry swagger file of standard ALTO protocol
  ([RFC7285](https://tools.ietf.org/html/rfc7285)).
- [api/ext/unicorn.yaml](https://github.com/openalto/alto-swagger/raw/spec/api/ext/unicorn.yaml) is
  the entry swagger file of the Unicorn extended protocol for cross-domain
  purpose.
- [api/ext/unicorn-standalone.yaml](https://github.com/openalto/alto-swagger/raw/spec/api/ext/unicorn-standalone.yaml)
  is a single swagger specification file which combines all references of
  `api/ext/unicorn.yaml`.
- [api/ext/1.2/unicorn.json](https://github.com/openalto/alto-swagger/raw/spec/api/ext/1.2/unicorn.json)
  is the resource listing file of the Unicorn extended protocol on Swagger
  Specification 1.2.
