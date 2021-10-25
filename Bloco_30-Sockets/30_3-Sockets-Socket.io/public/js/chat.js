// Esse código javascript determina que ao clicar no botão submit do formulário, será enviado um evento clientMessage com a mensagem preenchida no campo com id messageInput . Vamos preparar nosso back-end para receber este evento.

const socket = window.io();

const form = document.querySelector('form');
const inputMessage = document.querySelector('#messageInput');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  socket.emit('clientMessage', inputMessage.value);
  inputMessage.value = '';
  return false;
});

const createMessage = (message) => {
  const messagesUl = document.querySelector('#messages');
  const li = document.createElement('li');
  li.innerText = message;
  messagesUl.appendChild(li);
};

socket.on('serverMessage', (message) => createMessage(message));

window.onbeforeunload = function(event) {
  socket.disconnect();
};