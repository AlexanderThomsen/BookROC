import './LandingPage.css';

export default function LandingPage() {
  return (
    <div className="landing-in-wrapper">
      <section className="hero">
        <h1>Velkommen til vores app</h1>
        <p>Dette er et simpelt eksempel på en centreret landingpage.</p>
        <button className="cta-button">Kom i gang</button>
      </section>

      <section className="features">
        <div className="feature-card">
          <h2>Feature 1</h2>
          <p>Beskrivelse af feature 1.</p>
        </div>
        <div className="feature-card">
          <h2>Feature 2</h2>
          <p>Beskrivelse af feature 2.</p>
        </div>
        <div className="feature-card">
          <h2>Feature 3</h2>
          <p>Beskrivelse af feature 3.</p>
        </div>
      </section>
    </div>
  );
}
