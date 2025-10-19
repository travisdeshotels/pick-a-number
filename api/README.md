# Pick A Number API

## Stack used
* SQLITE
* Python
* fastapi

## Running the API
1. `make builddb` to set up the SQLITE database. Output file is `game.db`.
2. `python3 -m venv venv && source venv/bin/activate` to create a Python virtual environment and activate it.
3. `make build` to install the dependencies.
4. `export SQLITE_DB=/path/to/your/game.db` to set your database file path.
5. `make run` to start the server. 

## Usage
See [curl](doc/curl/commands.md) command examples.
