SWAGGER_VERSION=2.2.3
SWAGGER_LANG=python-flask
SWAGGER_CONFIG=config.json
SWAGGER_SPEC_URL="https://github.com/openalto/alto-swagger/raw/spec/api/ext/unicorn-standalone.yaml"

all: generate

generate: .bin/swagger-codegen-cli-${SWAGGER_VERSION}.jar
	PATH=.bin:${PATH}
	${SWAGGER_EXEC} generate -i ${SWAGGER_SPEC_URL} -l ${SWAGGER_LANG} -c ${SWAGGER_CONFIG}

.bin/swagger-codegen-cli-${SWAGGER_VERSION}.jar:
ifeq (${SWAGGER_EXEC}, "")
	curl http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar \
		--create-dirs -o .bin/swagger-codegen-cli-${SWAGGER_VERSION}.jar
	echo -e "#!/bin/bash\njava -jar swagger-codegen-cli-${SWAGGER_VERSION}.jar \$@" > .bin/swagger-codegen
	chmod +x .bin/swagger-codegen
	SWAGGER_EXEC=swagger-codegen
endif
