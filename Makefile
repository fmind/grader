PACKAGE=$(shell ./setup.py --name)
  
all: test type lint sort cover format package;

venv:
	python3.7 -m venv venv --clear
	venv/bin/pip install --editable .
	venv/bin/pip install -r requirements.txt
	jupyter nbextension enable --py widgetsnbextension --sys-prefix

test: venv
	venv/bin/pytest tests

type: venv
	venv/bin/mypy --ignore-missing-imports ${PACKAGE}

lint: venv
	venv/bin/pylint ${PACKAGE}

sort: venv
	venv/bin/isort --apply --recursive ${PACKAGE}

cover: venv
	venv/bin/coverage run --branch --source ${PACKAGE} -m pytest
	venv/bin/coverage report --omit=*/__main__.py --fail-under=0 

format: venv
	venv/bin/black --quiet --line-length 79 ${PACKAGE}

add:
	git add --all ${PACKAGE}/*.py

hook:
	git config core.hooksPath hooks/

work:
	venv/bin/jupyter notebook

clean:
	find . -name '*.whl' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

package: venv
	venv/bin/python setup.py bdist_wheel --universal

publish: clean package
	venv/bin/twine upload --repository pypi dist/*.whl
