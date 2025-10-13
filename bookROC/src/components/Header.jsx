import { useState } from 'react';
import './Header.css';

function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => setMenuOpen(!menuOpen);

  return (
    <header className="container">
      <div className="container-left">
        <img src="https://via.placeholder.com/100x40?text=Logo" alt="Logo" />
      </div>

      <div className="container-center desktop-menu">
        <div className="item">Hjem</div>
        <div className="item">Om</div>
        <div className="item">Kontakt</div>
      </div>

      <div className="container-right">
        <div className="desktop-login item">Login</div>

        {/* Hamburger / X button */}
        <button className="mobile-menu-button" onClick={toggleMenu}>
          {menuOpen ? '✖' : '☰'}
        </button>
      </div>

      <div className={`mobile-menu-overlay ${menuOpen ? 'open' : 'closed'}`}>
        <div className="mobile-menu-items">
          <div className="item" onClick={toggleMenu}>Hjem</div>
          <div className="item" onClick={toggleMenu}>Om</div>
          <div className="item" onClick={toggleMenu}>Kontakt</div>
          <div className="item" onClick={toggleMenu}>Login</div>
        </div>
      </div>
    </header>
  );
}

export default Header;
