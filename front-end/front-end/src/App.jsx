import React, { useState } from "react";
import "./index.css"; // Make sure this line is present!

function App() {
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResponse(null);
    try {
      const res = await fetch("http://localhost:8000/generate-video", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ story }),
      });
      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err.message || "An error occurred");
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="card">
        <h2 className="card-title">AI Story-to-Video Generator</h2>
        <form onSubmit={handleSubmit}>
          <label htmlFor="story">Paste your story:</label>
          <textarea
            id="story"
            rows={7}
            className="story-textarea"
            placeholder="Paste your story here..."
            value={story}
            onChange={e => setStory(e.target.value)}
            required
          />
          <button
            type="submit"
            className="button"
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate Video"}
          </button>
        </form>
        {error && <div className="error">{error}</div>}
        {response && (
          <div className="response">
            <h4 style={{ marginBottom: 10, fontWeight: 700, color: "#233865" }}>Backend Response:</h4>
            <pre>{JSON.stringify(response, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
