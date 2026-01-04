from fastapi import APIRouter
from cache.lru_cache import LRUCache
from services.data_service import fetch_slow_data

router = APIRouter()
cache=LRUCache(capacity=5)

@router.get("/data")
def get_data(q:str):
    cached = cache.get(q)

    if cached:
        return {
            "source":"cache",
            "data":cached
        }
    result=fetch_slow_data(q)
    cache.put(q,result)
    return {
        "source":"fresh",
        "data":result
    }
@router.get("/cache/stats")
def cache_stats():
    return {
        "capacity": cache.capacity,
        "current_size": len(cache.cache),
        "hits": cache.hits,
        "misses": cache.misses
    }