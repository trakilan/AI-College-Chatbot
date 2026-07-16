async function sendMessage() {

    const input = document.getElementById("question");
    const chatBox = document.getElementById("chat-box");
    const sendBtn = document.getElementById("sendBtn");

    const question = input.value.trim();

    if (question === "") {
        return;
    }

    // Show user's message
    chatBox.innerHTML += `
        <div class="user-message">
            ${question}
        </div>
    `;

    // Clear input
    input.value = "";
    sendBtn.disabled = true;
sendBtn.innerText = "Thinking...";

    // Show typing animation
    chatBox.innerHTML += `
        <div class="bot-message" id="typing">
            AI is typing...
        </div>
    `;

    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        // Send question to backend
        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        // Remove typing animation
        const typing = document.getElementById("typing");
        if (typing) {
            typing.remove();
        }

        // Show AI response
        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.answer}
            </div>
        `;

        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;
        sendBtn.disabled = false;
        sendBtn.innerText = "Send";

    } catch (error) {

        // Remove typing animation
        const typing = document.getElementById("typing");
        if (typing) {
            typing.remove();
        }

        // Show error message
        chatBox.innerHTML += `
            <div class="bot-message">
                Error connecting to backend.
            </div>
        `;
        sendBtn.disabled = false;
        sendBtn.innerText = "Send";


    }
}

// Press Enter to send message
document.getElementById("question").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});
function clearChat() {

    document.getElementById("chat-box").innerHTML = `
        <div class="bot-message">
            Hello! Ask me anything about the college.
        </div>
    `;

}