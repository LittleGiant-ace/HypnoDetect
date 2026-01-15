// ================================
// DOM REFERENCES (PERMANENT)
// ================================
const inputEl = document.getElementById("inputText");
const analyzeBtn = document.getElementById("analyzeBtn");
const resultBox = document.getElementById("result");


// ================================
// MOCK ML RESPONSE (TEMPORARY)
// ================================
function getMockMLResponse(text) {
  const lower = text.toLowerCase();

  let signals = [];
  let score = 0;

  if (lower.includes("as you breathe")) {
    signals.push({ type: "induction", phrase: "as you breathe" });
    score += 20;
  }

  if (lower.includes("trust me")) {
    signals.push({ type: "persuasion", phrase: "trust me" });
    score += 10;
  }

  if (lower.includes("without realizing")) {
    signals.push({ type: "subliminal", phrase: "without realizing" });
    score += 10;
  }

  score = Math.min(score, 100);

  let level = "Low";
  if (score > 60) level = "High";
  else if (score > 20) level = "Medium";

  return {
    score,
    level,
    signals,
    source: "mock-ml"
  };
}


// ================================
// FORMAT RESULT (PERMANENT)
// ================================
function formatResult(result) {
  let output = `Hypnosis Level: ${result.score}% (${result.level})\n\n`;

  if (result.signals.length > 0) {
    output += "Detected Signals:\n";
    result.signals.forEach(s => {
      const message = s.explanation || s.phrase || "Additional risk detected";
      output += `• [${s.type}] ${message}\n`;
    });
  } else {
    output += "No hypnosis patterns detected";
  }

  return output;
}


// ================================
// TYPEWRITER EFFECT (PERMANENT)
// ================================
function typeWriter(text, element, speed = 18) {
  element.textContent = "";
  let i = 0;

  const timer = setInterval(() => {
    element.textContent += text.charAt(i);
    i++;
    if (i >= text.length) clearInterval(timer);
  }, speed);
}


// ================================
// UI RENDERER (PERMANENT)
// ================================
function renderResult(result) {
  resultBox.innerHTML = "";
  resultBox.className = "show";

  const box = document.createElement("div");
  box.classList.add(
    result.score > 60 ? "score-high" :
    result.score > 20 ? "score-medium" :
    "score-low"
  );

  resultBox.appendChild(box);
  typeWriter(formatResult(result), box);
}

async function getAnalysisResult(text) {
  const response = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  return await response.json();
}


// ================================
// EVENT (PERMANENT)
// ================================
analyzeBtn.addEventListener("click", async () => {
  const text = inputEl.value.trim();
  if (!text) return;

  // THIS IS THE SWAP POINT LATER
  const analysisResult = await getAnalysisResult(text);
  renderResult(analysisResult);
});
