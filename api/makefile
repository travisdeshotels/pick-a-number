builddb:
	python3 db/initdb.py game.db

clean:
	rm -rf __pycache__ .venv

run:
	cd src; uv run uvicorn main:app --reload --host localhost
