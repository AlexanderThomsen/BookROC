import Footer from "./components/Footer";
import Header from "./components/header";
import LandingPage from "./components/LandingPage";
import "./App.css"; // global CSS

function App() {
  return (
    <div className="app-wrapper">
      <Header />
      <main className="landing-wrapper">
        <LandingPage />
      </main>
      <Footer />
    </div>
  );
}


export default App;
