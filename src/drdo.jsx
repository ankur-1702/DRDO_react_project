
import React from "react";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Footer from "./components/Footer";
import "./styles.css";

function App() {
  return (
    <div className="app-container">
   
      <video autoPlay muted loop className="background-video">
        <source src="/images/bg-video.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>


      <div className="content-overlay">
        <Header />
        <Navbar />
        <Hero />
        <Footer />
      </div>
    </div>
  );
}

export default App;
