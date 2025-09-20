build:
	pip install -r requirements.txt

builddb:
	python3 db/initdb.py game.db

clean:
	rm -rf __pycache__

run:
	cd src; uvicorn main:app --reload --host localhost
