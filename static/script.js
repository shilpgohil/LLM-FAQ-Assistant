document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("query-input");
    input.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendQuery();
        }
    });
});


let chatMemory = [];

function sendQuery() {
    const query = document.getElementById("query-input").value;
    if (!query) return;
    
    const chatLog = document.getElementById("chat-log");
    const userMessage = document.createElement("p");
    userMessage.textContent = "You: " + query;
    chatLog.appendChild(userMessage);
    
  
    chatMemory.push({ role: "user", content: query });
    
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: chatMemory })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.error || "Unknown error"); });
        }
        return response.json();
    })
    .then(data => {
        chatMemory.push({ role: "bot", content: data.response });
        updateChatLog();
    })
    .catch(error => {
        console.error("Chat error:", error.message);
    });
    
    
    document.getElementById("query-input").value = "";
}
function updateChatLog() {
    const chatLog = document.getElementById("chat-log");
    chatLog.innerHTML = ''; 
    chatMemory.forEach(message => {
        const messageElement = document.createElement("p");
        messageElement.textContent = `${message.role === 'user' ? 'You' : 'Bot'}: ${message.content}`;
        chatLog.appendChild(messageElement);
    });
}