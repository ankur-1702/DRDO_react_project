// src/components/Navbar.jsx
import React from "react";
import "../styles.css";

function Navbar() {
  return (
    <nav className="main-navbar">
      <ul className="nav-links">
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">DRDO</a>
        </li>
        <li>
          <a href="#">Organisation</a>
        </li>
        <li>
          <a href="#">Outreach</a>
        </li>
        <li>
          <a href="#">Careers</a>
        </li>
        <li>
          <a href="#">Publications</a>
        </li>
        <li>
          <a href="#">RTI</a>
        </li>
        <li>
          <a href="#">Contact Us</a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
