i:
	# install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
r:
	python main.py
format:
	# format code
	black *.py mylib/*.py
lint:
	# flake8 or # pylint
	pylint --disable=R, C *.py mylib/*.py
test:
	# test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	# build container
	docker build -t deploy-fastapi .
run:
	# run docker
	docker run -p 127.0.0.1:8080:8080 a92690211e75
deploy:
	# deploy
all: install lint test deploy