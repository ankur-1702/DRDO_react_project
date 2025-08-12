// src/components/Hero.jsx
import React from "react";
import "../styles.css";

function Hero() {
  return (
    <div className="hero-container">
      <div className="question-box">
        <h1 className="question-title">What's on your mind?</h1>
        <div className="input-area">
          <input
            type="text"
            placeholder="Type your question..."
            className="question-input"
          />
          <button className="send-button">Send</button>
        </div>
      </div>
    </div>
  );
}

export default Hero;
