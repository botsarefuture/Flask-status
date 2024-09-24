# Flask Status Package

A simple Flask add-on that provides a status page to monitor the health of your web application, including system metrics and database connectivity.

## Features

- **System Health Checks**: Provides real-time metrics such as CPU usage and available memory.
- **Database Connection**: Monitors MongoDB connectivity.
- **HTTP Status Codes**: Returns `200` if everything is fine, and `500` if there is an issue with the system or the database connection.

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/botsarefuture/Flask-status.git
    cd Flask-status
    ```

2. Install the package and its dependencies:

    ```bash
    pip install -e .
    ```

3. Add the following dependencies to your project's `requirements.txt` if you're using one:

    ```
    Flask
    psutil
    pymongo
    ```

## Usage

To integrate the `Status` class into your Flask application, follow these steps:

1. **Initialize the Status Package**:

    ```python
    from flask import Flask
    from status_package import Status

    app = Flask(__name__)

    # Initialize the status checker
    status = Status(app)

    if __name__ == '__main__':
        app.run(debug=True)
    ```

2. **Custom MongoDB URI** (optional):

    You can also pass a custom MongoDB URI to the `Status` class during initialization:

    ```python
    status = Status(app, mongo_uri="mongodb://your-custom-uri")
    ```

3. **Access the Status Page**:

    Once your Flask app is running, visit the `/status` endpoint to see real-time system and database information:

    ```
    http://localhost:5000/status
    ```

## Status Response

The `/status` endpoint returns a JSON object with the following structure:

```json
{
    "app_status": "running",
    "database_connected": true,
    "system_metrics": {
        "cpu_usage": 15.3,
        "memory_available": 2147483648,
        "memory_total": 8589934592
    }
}
```

If an issue occurs (e.g., high CPU usage or a database connection failure), the endpoint returns a `500` HTTP status code, along with relevant information in the response body.

## File Structure

Here’s the project tree for the `status_package`:

```
status_package/
├── status_package/
│   ├── __init__.py
│   ├── status.py
│   └── checks.py
├── tests/
│   └── test_status.py
├── setup.py
├── README.md
└── requirements.txt
```

- **`status.py`**: Main class for handling `/status` route and logic.
- **`checks.py`**: Contains helper functions for system and database checks.
- **`test_status.py`**: Unit tests for status checks using `pytest`.

## Testing

To run the tests:

1. Install `pytest`:

    ```bash
    pip install pytest
    ```

2. Run the tests:

    ```bash
    pytest
    ```

## Requirements

- Python 3.7+
- Flask
- psutil (for system metrics)
- pymongo (for MongoDB connectivity)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.