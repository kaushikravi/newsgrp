from main import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World! Basic Test for MSDS 498'
    assert response.status_code == 200
