function toggleGroup(btn) {
  const items = btn.nextElementSibling;
  items.style.display = items.style.display === 'none' ? 'block' : 'none';
}

function selectItem(el) {
  document.querySelectorAll('.inbox-item').forEach(i => i.classList.remove('active'));
  el.classList.add('active');
}

function toggleSidebar() {
  document.getElementById('sidebar-body').classList.toggle('collapsed');
}

let currentType = null;

function activateReply(btn, type) {
  currentType = type;
  document.querySelectorAll('.action-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');

  const textarea = document.querySelector('.reply-input');
  const sendBtn  = document.querySelector('.send-btn');
  textarea.disabled = false;
  sendBtn.disabled  = false;
  textarea.placeholder = `Write your ${type} response ...`;
  textarea.focus();
  document.querySelector('.reply-footer').classList.remove('bg-light');
}

function sendUpdate() {
  const textarea = document.querySelector('.reply-input');
  const message  = textarea.value.trim();
  if (!message) return;

  const thread = document.querySelector('.message-thread');

  // Append outgoing message
  appendMessage(thread, message, 'outgoing');

  // Reset UI
  textarea.value    = '';
  textarea.disabled = true;
  textarea.placeholder = 'Write a response ...';
  document.querySelector('.send-btn').disabled = true;
  document.querySelector('.reply-footer').classList.add('bg-light');
  document.querySelectorAll('.action-btn').forEach(b => b.classList.remove('selected'));


}

function appendMessage(thread, text, direction) {
  const wrap = document.createElement('div');
  wrap.className = `message-wrap ${direction}`;

  const bubble = document.createElement('div');
  bubble.className = 'message-bubble';
  bubble.textContent = text;

  const time = document.createElement('span');
  time.className = 'message-time';
  time.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  wrap.appendChild(bubble);
  wrap.appendChild(time);
  thread.appendChild(wrap);
  thread.scrollTop = thread.scrollHeight;
  return wrap;
}