import requests

url = 'http://localhost:5005/webhooks/rest/webhook'

# Send initial user message
data = {
    'sender': 'user',
    'message': 'Hi'
}
response = requests.post(url, json=data)

# Collect conversation history
conversation = response.json()

# Continue the conversation by sending more messages
data = {
    'sender': 'user',
    'message': 'What can you do?'
}
response = requests.post(url, json=data)
conversation.extend(response.json())

# You can collect as many messages as needed

# Save conversation history to a file
with open('conversation_history.json', 'w') as file:
    json.dump(conversation, file)
