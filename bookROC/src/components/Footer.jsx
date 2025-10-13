import React from "react";
import "./Footer.css"; // separat CSS til footeren

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>© 2025 BookROC. All rights reserved.</p>
        <nav className="footer-nav">
          <a href="#home">Home</a>
          <a href="#books">Books</a>
          <a href="#users">Users</a>
          <a href="#contact">Contact</a>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;
