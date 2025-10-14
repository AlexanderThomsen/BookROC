import React from "react";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2 className="sidebar-logo">BookROC</h2>
      <ul className="sidebar-menu">
        <li className="menu-item">🏠 Hjem</li>
        <li className="menu-item">🔍 Udforsk bøger</li>
        <li className="menu-item">📚 Mine bøger</li>
        <li className="menu-item">📝 Anmeldelser</li>
        <li className="menu-item">⚙️ Indstillinger</li>
        <li className="menu-item">⭐ Favoritter</li>
        <li className="menu-item">🔔 Notifikationer</li>
        <li className="menu-item">🚪 Log ud</li>
      </ul>
    </div>
  );
};

export default Sidebar;
