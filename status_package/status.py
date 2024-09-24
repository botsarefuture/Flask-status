import psutil
from flask import jsonify
from pymongo import MongoClient, errors

class Status:
    def __init__(self, app=None, mongo_uri="mongodb://localhost:27017/mydb"):
        """
        Initialize the Status class with an optional Flask app and MongoDB URI.
        """
        self.app = app
        self.mongo_uri = mongo_uri
        self.mongo_client = MongoClient(self.mongo_uri, serverSelectionTimeoutMS=1000)
        
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize the app by registering the /status route.
        """
        app.add_url_rule('/status', 'status', self.status)

    def check_database_connection(self):
        """
        Check if the MongoDB database is reachable.
        Returns True if the connection is successful, False otherwise.
        """
        try:
            self.mongo_client.admin.command('ping')
            return True
        except errors.ServerSelectionTimeoutError:
            return False

    def get_system_metrics(self):
        """
        Fetch system CPU and memory metrics.
        Returns a dictionary with the data.
        """
        return {
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_available': psutil.virtual_memory().available,
            'memory_total': psutil.virtual_memory().total
        }

    def status(self):
        """
        Health check endpoint. 
        Returns JSON with system metrics and database status.
        """
        system_metrics = self.get_system_metrics()
        db_connected = self.check_database_connection()

        status_data = {
            'app_status': 'running',
            'database_connected': db_connected,
            'system_metrics': system_metrics
        }

        # Determine if something is wrong
        if not db_connected or system_metrics['cpu_usage'] > 90:
            return jsonify(status_data), 500

        return jsonify(status_data), 200
