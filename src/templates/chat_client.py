html = '''
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>FastApi Chat client</title>
    </head>
    <body>
      <h1>WebSocket Chat</h1>
      <form action="" onsubmit="sendMessage(event)">
        <textarea id="messageText" autocomplete="off" /></textarea>
        <button>Send</button>
      </form>
      <ul id="messages"></ul>
      <script>
        const ws = new WebSocket('ws://localhost:8000/chat/chatroom');
        ws.onmessage = function (event) {
          const messages = document.getElementById('messages');
          const message = document.createElement('li');
          const content = document.createTextNode(event.data);
          message.appendChild(content);
          messages.appendChild(message);
        };
        function sendMessage(event) {
          const input = document.getElementById('messageText');
          ws.send(input.value);
          input.value = '';
          event.preventDefault();
        }
      </script>
    </body>
  </html>
'''
