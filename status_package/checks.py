import psutil
from pymongo import MongoClient, errors

def check_database_connection(mongo_uri):
    """
    Check if MongoDB is reachable.
    """
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=1000)
    try:
        client.admin.command('ping')
        return True
    except errors.ServerSelectionTimeoutError:
        return False

def get_system_metrics():
    """
    Get system CPU and memory stats.
    """
    return {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_available': psutil.virtual_memory().available,
        'memory_total': psutil.virtual_memory().total
    }
