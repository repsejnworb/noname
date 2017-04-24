NAME = noname
VERSION ?= $(shell git describe --always)
VERSION := $(subst -,.,$(VERSION))

all: run

prepare: version.py


version.py:
	echo "__version__ = '$(VERSION)'" > $(NAME)/version.py

env: version.py
	test -d env || virtualenv env -p /usr/bin/python2.7
	./env/bin/pip install -Ur requirements/development.txt
	./env/bin/python setup.py develop

run: env
	./env/bin/$(NAME)

check: env
	./env/bin/flake8 $(NAME)

coverage: env
	./env/bin/py.test --junitxml=junitxml-result.xml \
						--cov-report html \
						--cov-report xml \
						--cov-report term \
						--cov vastd vastd

clean:
	rm -rf build dist env *.egg-info
	find . -name *.py[oc] -delete
	rm -f vastd/version.py

