from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from sessions import add_chat, all_chat

chat = APIRouter()


html = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="messageText" autocomplete="off"/>
        <button>Send</button>
    </form>
    <ul id='messages'></ul>
    <script>
        var ws = new WebSocket("ws://192.168.42.117:8000/ws");
        var messagesList = document.getElementById('messages');

        // Function to load and render messages from localStorage
        function loadMessages() {
            const savedMessages = JSON.parse(localStorage.getItem('chatMessages')) || [];
            messagesList.innerHTML = ''; // Clear existing messages
            savedMessages.forEach(msg => {
                renderMessage(msg);
            });
        }

        // Function to render a single message
        function renderMessage(msg) {
            var message = document.createElement('li');
            var content = document.createTextNode(msg);
            message.appendChild(content);
            messagesList.appendChild(message);
        }

        // Initialize by loading messages
        loadMessages();

        // Handle incoming WebSocket messages
        ws.onmessage = function(event) {
            const message = event.data;
            
            // Save the message to localStorage
            const savedMessages = JSON.parse(localStorage.getItem('chatMessages')) || [];
            savedMessages.push(message);
            localStorage.setItem('chatMessages', JSON.stringify(savedMessages));

            // Render the new message
            renderMessage(message);
        };

        // Send a message through WebSocket
        function sendMessage(event) {
            var input = document.getElementById("messageText");
            ws.send(input.value);

            // Optionally add the sent message to localStorage for user history
            const savedMessages = JSON.parse(localStorage.getItem('chatMessages')) || [];
            savedMessages.push(input.value);
            localStorage.setItem('chatMessages', JSON.stringify(savedMessages));

            input.value = '';
            event.preventDefault();
        }

        // Synchronize messages across tabs
        window.addEventListener('storage', function(event) {
            if (event.key === 'chatMessages') {
                loadMessages();
            }
        });
    </script>
</body>
</html>

"""
@chat.get("/")
async def get_page():
    return HTMLResponse(html)


@chat.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        texts = websocket.receive_text()
        data = await add_chat(texts)
        # await websocket.send_text(f"Message received: {data}")
