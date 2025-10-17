import React, { useEffect, useState } from 'react';
import './HomePage.css';
import Logo from '../assets/mini_billede.jpg';

const HomePage = () => {
  const [username, setUsername] = useState('');

  useEffect(() => {
    // Hent bruger info fra localStorage
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      const userObj = JSON.parse(storedUser);
      setUsername(userObj.name || userObj.email || 'Bruger'); // fallback hvis name ikke findes
    }
  }, []);

  return (
    <div className="homepage-container">
      {/* Hero Section */}
        <section className="hero-section">
        <div className="hero-content">
            <h1>Velkommen {username}!</h1>
            <p>
            Start din egen bogsamling i dag, og del dine favoritter med venner. Det har aldrig været nemmere at holde styr på bøger du elsker
            </p>
            <div className="hero-buttons">
            <button 
                className="btn-primary" 
                onClick={() => window.location.href='/books'} // eller brug navigate('/books')
            >
                Opret din samling
            </button>
            </div>
        </div>
        <div className="hero-image">
            <img src={Logo} alt="Logo" />
        </div>
        </section>


      {/* Eksempel på sektion */}
      <section className="features-section">
        <div className="feature">
          <h2>Find Bøger</h2>
          <p>Søg blandt tusindvis af bøger på platformen.</p>
        </div>
        <div className="feature">
          <h2>Opret Samlinger</h2>
          <p>Lav dine egne samlinger og del med venner.</p>
        </div>
        <div className="feature">
          <h2>Anbefalinger</h2>
          <p>Få personlige boganbefalinger baseret på dine interesser.</p>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
