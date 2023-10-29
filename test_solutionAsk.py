import requests

# Task to be solved
data = {
    "task": "Configuring Spam Fitlers to Reduce Unwanted Email"
}

# Sending request to the /serpapi endpoint
response = requests.post("http://127.0.0.1:8000/serpapi/", json=data)
print("Status code:", response.status_code)
print("Task:", data["task"])
print("Solution:", response.json()['result'])
