import requests

# Task to be solved
data = {
    "task2": "Configuring Spam Fitlers to Reduce Unwanted Email"
}

# Sending request to the /serpapi endpoint
response = requests.post("http://127.0.0.1:8000/tavily/", json=data)
print("Status code:", response.status_code)
print("Task:", data["task2"])
print("Solution:", response.json()['result'])
