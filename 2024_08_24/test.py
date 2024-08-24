import os

os.environ['REDIS_HOST'] = '127.0.0.1'
os.environ['REDIS_PASSWORD'] = '你的密码'

print(f"REDIS_HOST: {os.getenv('REDIS_HOST')}")
print(f"REDIS_PASSWORD: {os.getenv('REDIS_PASSWORD')}")
