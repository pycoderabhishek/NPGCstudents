
function sendMessage() {
    const userInput = document.getElementById('userInput');
    const messages = document.getElementById('messages');

    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    // Add user message to the chat
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user-message';
    userMessageDiv.textContent = userMessage;
    messages.appendChild(userMessageDiv);

    // Fetch bot response
    fetch("https://npgcstudents.pythonanywhere.com/chatbot/get_response/?message=" + encodeURIComponent(userMessage))
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.response) {
            const botMessageDiv = document.createElement('div');
            botMessageDiv.className = 'message bot-message';
            botMessageDiv.textContent = data.response;
            messages.appendChild(botMessageDiv);
        } else {
            console.error("Unexpected response format:", data);
        }
    })
    .catch(error => {
        console.error("Error fetching bot response:", error);
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.className = 'message bot-message';
        errorMessageDiv.textContent = "Sorry, there was an issue contacting the chatbot.";
        messages.appendChild(errorMessageDiv);
    });

}

// Function to show the default bot message when the page loads
function showDefaultMessage() {
    const messages = document.getElementById('messages');
    
    // Prevent duplicate default message
    if (messages.children.length > 0) return;

    const defaultMessage = document.createElement('div');
    defaultMessage.className = 'message bot-message';
    defaultMessage.textContent = "Hey there! I'm your college chatbot at your assistance. Ask me anything! You can ask me about fees, admissions, deadlines, and more.";
    messages.appendChild(defaultMessage);
}

// Run the default message function when the page loads
document.addEventListener("DOMContentLoaded", showDefaultMessage);
