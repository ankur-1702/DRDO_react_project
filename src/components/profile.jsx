// src/components/Profile.jsx
import React from "react";
import "./profiles.css";

export default function Profile() {
  return (
    <div className="profile-container">
      <img
        src="https://www.w3schools.com/howto/img_avatar.png"
        alt="User Profile"
        className="profile-avatar"
      />
      <span className="profile-name">Ankur</span>
    </div>
  );
}
