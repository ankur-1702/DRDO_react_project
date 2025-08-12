import React, { useState } from "react";
import "./ProfileDropdown.css";

const ProfileDropdown = () => {
  const [open, setOpen] = useState(false);

  return (
    <div className="profile-container" onClick={() => setOpen(!open)}>
      <img
        src="https://www.w3schools.com/howto/img_avatar.png"
        alt="Profile"
        className="profile-avatar"
      />
      <span className="profile-name">Ankur ▾</span>

      {open && (
        <div className="dropdown-menu">
          <div className="dropdown-item">My Profile</div>
          <div className="dropdown-item">Settings</div>
          <div className="dropdown-item">Logout</div>
        </div>
      )}
    </div>
  );
};

export default ProfileDropdown;
