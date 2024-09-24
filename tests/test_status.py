import pytest
from status_package.status import Status
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    status = Status(app)
    return app

def test_status_endpoint(client):
    response = client.get('/status')
    assert response.status_code in [200, 500]
    assert 'system_metrics' in response.json
