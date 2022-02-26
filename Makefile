run:
	flask run --port 8080 --host 0.0.0.0
# 	python3 app.py
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C,W app.py