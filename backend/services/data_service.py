import time
def fetch_slow_data(query: str):
    time.sleep(2)
    return {
        "query": query,
        "result": f"Data for {query}"
    }