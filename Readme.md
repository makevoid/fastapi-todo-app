# FastAPI sample to-do list app

Sample To-do list application featuring:

- FastAPI
- mako
- pyHaml
- python 3
- vanilla js
- axios
- redis
- json
- docker

Note: If you're looking for the Flask version of this To-Do app then visit: https://github.com/makevoid/flask-todo-app


### Install

soon I will add a requirements.txt file for now you will need to install from docker or execute pip install manually of all the dependencies

    pip install uvicorn fastapi aiofiles python-multipart redis mako git+https://github.com/mikeboers/pyhaml

### Prerequisites

You need to have Redis running locally listening on the default port 6379.

### Run

   ./run

This will run the python app via `uvicorn`.

Then visit http://localhost:3000

### Docker

Build and run:

    docker-compose up --build

#### Redis

Connect to dev redis

    redis-cli -p 6380

---

Enjoy!

@makevoid
