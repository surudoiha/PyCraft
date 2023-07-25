import redis

class RedisClient:
    def __init__(self, host, port):
        self.db = redis.Redis(host=host, port=port)

    def set_value(self, key, value):
        self.db.set(key, value)

    def get_value(self, key):
        return self.db.get(key)
