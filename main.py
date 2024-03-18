from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from huey import RedisHuey

app = FastAPI()
redis = Redis(host='redis', port=6379, db=0)
huey = RedisHuey('my-app', host='redis')

class Item(BaseModel):
    value: str

@huey.task()
def add_key_value(key, value):
    redis.set(key, value)
    return f"Added {key}: {value}"

@app.get("/get/{key}")
async def read_item(key: str):
    value = redis.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"key": key, "value": value.decode("utf-8")}

@app.post("/set/{key}")
async def write_item(key: str, item: Item):
    result = add_key_value(key, item.value)
    return {"task_id": result.id, "status": "queued"}
