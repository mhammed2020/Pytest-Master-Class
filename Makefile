install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# python -m pytest -vv --cov=hello  test_hello.py
	# python -m pytest -vv --cov=hello  tests
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval notebook.ipynb

debug:
	python -m pytest -vv --pdb  

debugthree:
	python -m pytest -vv --pdb  --maxfail=4

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test format