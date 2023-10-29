import requests

# Task to be searched
data = {
    "task_description": "external hard drive not recognized"
}

# Sending request to the /search endpoint
response = requests.post("http://127.0.0.1:8000/search/", json=data)
print(response.status_code)
formatted_output = f"Your task to be searched: {data['task_description']}\n"
formatted_output += "The similar tasks found:\n" + "\n".join(response.json()['result'])
print(formatted_output)


