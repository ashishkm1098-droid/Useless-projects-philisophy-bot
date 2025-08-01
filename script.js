// // script.js - Connects your Keanu frontend to the Philosophical AI backend

document.getElementById("userInput").addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    askKeanu();
  }
});

// Add click handler for tools button (optional enhancement)
document.querySelector('.tools button').addEventListener('click', function() {
  showSampleQuestions();
});
function playMusic() {
  const audio = document.getElementById("bg-music");
  audio.volume = 100.0; // adjust volume
  audio.play();
}


function askKeanu() {
  const input = document.getElementById("userInput");
  const responseBox = document.getElementById("responseBox");
  const question = input.value.trim();

  if (!question) {
    responseBox.innerText = "Please enter a question.";
    return;
  }

  // Show pondering message with Keanu style
  responseBox.innerHTML = `
    <div class="pondering">
      🧘‍♂️ Keanu is pondering your question...
      <div class="thinking-dots">
        <span>.</span><span>.</span><span>.</span>
      </div>
    </div>
  `;

  // Add some CSS for the pondering animation if not already in style.css
  if (!document.querySelector('#pondering-style')) {
    const style = document.createElement('style');
    style.id = 'pondering-style';
    style.textContent = `
      .pondering {
        text-align: center;
        font-style: italic;
        color: #666;
        animation: pulse 1.5s infinite;
      }
      .thinking-dots {
        display: inline-block;
        margin-left: 5px;
      }
      .thinking-dots span {
        animation: blink 1.4s infinite both;
      }
      .thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
      .thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
      @keyframes pulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
      }
      @keyframes blink {
        0%, 80%, 100% { opacity: 0; }
        40% { opacity: 1; }
      }
      .keanu-response {
        font-size: 18px;
        line-height: 1.6;
        color: #333;
        background: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        margin-top: 10px;
        animation: fadeIn 0.5s ease-in;
      }
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
      }
      .sample-questions {
        margin-top: 20px;
        padding: 15px;
        background: #f0f0f0;
        border-radius: 10px;
      }
      .sample-questions h3 {
        margin-top: 0;
        color: #333;
      }
      .question-suggestion {
        display: inline-block;
        background: #e0e0e0;
        padding: 8px 12px;
        margin: 5px;
        border-radius: 15px;
        cursor: pointer;
        font-size: 14px;
        transition: background 0.3s ease;
      }
      .question-suggestion:hover {
        background: #d0d0d0;
      }
    `;
    document.head.appendChild(style);
  }

  // Make the API call to your Flask backend
  fetch("/llm", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  })
    .then(res => res.json())
    .then(data => {
      // Display the response with Keanu-style formatting
      responseBox.innerHTML = `
        <div class="keanu-response">
          🗣️ <strong>Keanu reflects:</strong><br>
          "${data.response}"
        </div>
      `;
    })
    .catch(err => {
      responseBox.innerHTML = `
        <div class="keanu-response" style="border-left-color: #f44336;">
          ❌ <strong>Connection Error:</strong><br>
          An error occurred while asking Keanu. Make sure your Flask server is running on http://localhost:5000
          <br><small>Error details: ${err.message}</small>
        </div>
      `;
      console.error("Error:", err);
    });

  // Clear the input
  input.value = "";
}

function showSampleQuestions() {
  const responseBox = document.getElementById("responseBox");
  
  const sampleQuestions = [
    "What is the meaning of life?",
    "How should I deal with suffering?",
    "What is true happiness?",
    "Do we have free will?",
    "What happens when we die?",
    "What is the nature of consciousness?",
    "How should I live my life?",
    "What is love?",
    "Why do we exist?",
    "What is the purpose of pain?"
  ];

  const questionsHTML = sampleQuestions.map(q => 
    `<span class="question-suggestion" onclick="askSampleQuestion('${q}')">${q}</span>`
  ).join('');

  responseBox.innerHTML = `
    <div class="sample-questions">
      <h3>🤔 Sample Questions for Keanu:</h3>
      ${questionsHTML}
      <p><small>Click on any question to ask Keanu</small></p>
    </div>
  `;
}

function askSampleQuestion(question) {
  const input = document.getElementById("userInput");
  input.value = question;
  askKeanu();
}

// Optional: Add some startup wisdom when the page loads
window.addEventListener('load', function() {
  const responseBox = document.getElementById("responseBox");
  
  const startupWisdom = [
    "The journey of a thousand miles begins with a single question.",
    "In seeking answers, we find ourselves asking better questions.",
    "Wisdom is not in having all the answers, but in asking the right questions.",
    "Every question is a doorway to understanding.",
    "The deepest truths often come disguised as simple questions."
  ];
  
  const randomWisdom = startupWisdom[Math.floor(Math.random() * startupWisdom.length)];
  
  responseBox.innerHTML = `
    <div class="keanu-response">
      🙏 <strong>Keanu welcomes you:</strong><br>
      "${randomWisdom}"
      <br><br>
      <small>The question is the key,
and the silence, the door.</small>
    </div>
  `;
});

// Optional: Add microphone functionality placeholder
document.querySelector('.actions button[title="Microphone"]').addEventListener('click', function() {
  alert('🎤 Voice input feature coming soon! For now, please type your question.');
});

// Optional: Add audio functionality placeholder
document.querySelector('.actions button[title="Audio"]').addEventListener('click', function() {
  alert('📶 Audio response feature coming soon! For now, responses are text-based.');
});