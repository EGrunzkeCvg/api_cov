def test_ping(test_client):
    resp = test_client.get("/ping")
    assert resp.status_code == 200
    assert resp.content == b'"pong"'
