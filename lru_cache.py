"""
Implementation of LRU Cache
"""

from collections import OrderedDict


class Cache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache_dic = OrderedDict()

    # get the item
    def get(self, key):
        """
          retrive the item from the dic. And if found since its recently been accessed re insert into the dict
        """
        item = self.cache_dic.get(key)
        if item is not None:
            self.put(key)
        return item

    def put(self, key):
        """
          check if item exists and if so remove first and add it back to the result dict to make sure they are recently accessed.
        """
        if key in self.cache_dic or len(self.cache_dic) >= self.cache_size:
            self.cache_dic.popitem(last=False)
        self.cache_dic[key] = key
        return self.cache_dic


lru_cache = Cache(cache_size=3)
print(lru_cache.put(1))
print(lru_cache.put(2))
print(lru_cache.put(3))
print(lru_cache.put(4))
print(lru_cache.get(2))
print(lru_cache.get(1))
print(lru_cache.put(5))

