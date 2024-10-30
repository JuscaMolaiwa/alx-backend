#!/usr/bin/env python3
"""
1. FIFO caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a caching system that stores items
    using a First-In-First-Out (FIFO) approach when
    the cache reaches its size limit.
    """
    
    def __init__(self):
        """Initializes the FIFO cache instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Stores an item in the cache.
        
        If the cache size exceeds the maximum limit,
        the earliest added entry is removed.
        """
        if key is None or item is None:
            return
        
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the oldest item in cache (FIFO)
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item from the cache by its key.
        
        Returns None if the key is not found.
        """
        return self.cache_data.get(key, None)

