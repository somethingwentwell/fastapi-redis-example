from fastapi import FastAPI  
from redis import Redis  
import random  
  
app = FastAPI()  
redis = Redis(host='redis', port=6379, db=0)  
  
@app.get("/generate")  
def generate_number():  
    number = random.randint(0, 10)  
    current_value = redis.get("number")  
    if current_value is None:  
        redis.set("number", number)  
    else:  
        new_value = int(current_value) + number  
        redis.set("number", new_value)  
    return {"number": number}  
  
@app.get("/number")  
def read_number():  
    number = redis.get("number")  
    return {"number": int(number) if number else None}  
