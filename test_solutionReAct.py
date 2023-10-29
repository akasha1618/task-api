import requests

# Task to be solved
data = {
    "task2": "hey its harry and i really dont know how to hande a hardware issue again this time its laptop screen flickering intermittently any suggestions on what to do next anyone free to help"
}

# Sending request to the /serpapi endpoint
response = requests.post("http://127.0.0.1:8000/tavily/", json=data)
print("Status code:", response.status_code)
print("Task:", data["task2"])
print("Solution:", response.json()['result'])
