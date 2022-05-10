import redis
import time

# Establish a connection to the Redis database 1 at
# redis://localhost:6379
r = redis.Redis(host='localhost', port=6379, db=1)
r.set('hello', 'world')
value = r.get('hello')
print(value) # b'world': binary value by the prefix b
print(value.decode())

# SET bye "In 60 seconds, I'll self-delete" EX 60
r.set('bye', "In 60 seconds, I'll self-delete", ex=60)
exp_msg = r.get('bye')
print(exp_msg.decode())

# wait 60 second
time.sleep(60)
exp_msg = r.get('bye')
print(exp_msg.decode()) # AttributeError: 'NoneType' object has no attribute 'decode'

r.delete('hello')  # 1: True
print(r.get('hello').decode())