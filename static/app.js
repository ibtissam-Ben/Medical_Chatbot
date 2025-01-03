const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

// Function to append messages to the chatbox
function appendMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');

    // Apply specific styles based on the sender (user or bot)
    if (sender === 'user') {
        messageDiv.classList.add('user-message');
    } else {
        messageDiv.classList.add('bot-message');
    }

    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    // Auto-scroll to the bottom of the chatbox
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to handle sending a message
async function sendMessage() {
    const query = userInput.value.trim();
    if (query !== "") {
        // Append user's message
        appendMessage(query, 'user');
        userInput.value = ""; // Clear the input field

        try {
            // Send the query to the backend
            const response = await fetch("http://127.0.0.1:5001/query", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query }),
            });

            if (response.ok) {
                const data = await response.json();
                // Append the bot's response
                appendMessage(data.answer, 'bot');
            } else {
                const errorData = await response.json();
                appendMessage(`Error: ${errorData.error || "Something went wrong"}`, 'bot');
            }
        } catch (error) {
            appendMessage("Error: Unable to reach the server. Please try again later.", 'bot');
        }
    }
}

// Function to handle pressing Enter to send the message
userInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
