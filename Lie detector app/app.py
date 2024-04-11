import requests

# Smoke testing part
response = requests.get("http://example.com/api/detect_lie?statement=I%20am%20telling%20the%20truth")
assert response.status_code == 200
assert response.json()["result"] == "Truth"

# Functionality testing part
response = requests.get("http://example.com/api/detect_lie?statement=I%20am%20lying")
assert response.status_code == 200
assert response.json()["result"] == "Lie"

# Performance testing part
import time
start_time = time.time()
for _ in range(100):
    requests.get("http://example.com/api/detect_lie?statement=I%20am%20telling%20the%20truth")
end_time = time.time()
assert end_time - start_time < 5  # Ensure the app responds within 5 seconds

# Security testing part
try:
    response = requests.get("http://example.com/api/detect_lie?statement='; DROP TABLE users;--")
    assert "error" not in response.text
except Exception as e:
    assert False, "Security vulnerability detected: " + str(e)
