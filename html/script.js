const chatBox = document.querySelector('.chat-box');
const chatInput = document.querySelector('.chat-input input');
const chatButton = document.querySelector('.chat-input button');

chatButton.addEventListener('click', () => {
  sendMessage();
});

chatInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

function sendMessage() {
  const message = chatInput
