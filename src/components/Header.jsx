import React from "react";
import ProfileDropdown from "./ProfileDropdown";
import "./Header.css"; 

function Header() {
  return (
    <header className="header">
      <div className="title-section">
        <h1>BODHAK AI</h1>
        <p>Translating Ideas Into Instincts...</p>
      </div>
      <ProfileDropdown />
    </header>
  );
}

export default Header;
