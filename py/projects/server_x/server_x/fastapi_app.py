import datetime
import logging

import uvicorn
from fastapi import FastAPI

import mycorp.server_schemas.schema_x as schema_x


LOGGER = logging.getLogger(__name__)


app = FastAPI()

@app.get("/")
async def root() -> str:
    return f"Alive at this time: {datetime.datetime.now()}"


@app.get("/stuff")
async def get_stuff() -> schema_x.Stuff:
    stuff = schema_x.Stuff(mystr="Hello, World!", myints=[1, 2, 3])
    return stuff


# Usually, run with:
#   uvicorn server_x.fastapi_app:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

