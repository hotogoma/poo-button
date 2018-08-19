AWS_PROFILE = default
FUNCTION = poo-button

.PHONY: default publish clean

default:

psycopg2:
	docker run --rm -v ${PWD}:/work -w /work python:3.6 pip install -r requirements.txt -t .

function.zip: main.py psycopg2
	zip -r $@ $^

publish: function.zip
	aws --profile ${AWS_PROFILE} lambda update-function-code \
		--function-name ${FUNCTION} \
		--zip-file fileb://$<

clean: function.zip
	rm -f $^
