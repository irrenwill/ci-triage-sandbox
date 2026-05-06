def test_passing():
    assert 1 + 1 == 2

def test_failing():
    result = {"status": 500, "error": "connection refused", "host": "db.internal:5432"}
    assert result["status"] == 200, f"API health check failed: {result}"
