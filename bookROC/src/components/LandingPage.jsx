import './LandingPage.css';

export default function LandingPage() {
  return (
    <div className="landing-in-wrapper">
      <section className="hero">
        <h1>Velkommen til BookROC</h1>
        <p>Din digitale platform til at organisere og udforske bøger på en nem og overskuelig måde.</p>
        <button className="cta-button">Kom i gang</button>
      </section>

      <section className="features">
        <div className="feature-card">
          <h2>Organiser dine bøger</h2>
          <p>Opret samlinger, kategoriser dine bøger og hold styr på, hvad du har læst eller vil læse.</p>
        </div>
        <div className="feature-card">
          <h2>Få anbefalinger</h2>
          <p>Basér dine valg på personlige anbefalinger og populære bøger blandt vores brugere.</p>
        </div>
        <div className="feature-card">
          <h2>Del med venner</h2>
          <p>Del dine bogsamlinger, læseoplevelser og anmeldelser med dine venner på platformen.</p>
        </div>
      </section>
    </div>
  );
}
