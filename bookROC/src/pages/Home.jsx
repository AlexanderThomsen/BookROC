import React, { useEffect, useState } from "react";
import Sidebar from "../components/sidebar";
import HomeCardBooks from "../components/HomeCardBooks";
import "./Home.css";

const Home = ({ userId }) => {
  const [userName, setUserName] = useState("");

  useEffect(() => {
    if (!userId) return;

    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUserName(data.username))
      .catch(err => console.error("Kunne ikke hente bruger:", err));
  }, [userId]);

  return (
    <div className="home-container">
      <Sidebar />
      <div className="home-main">
        <h1>Velkommen {userName || "til BookROC"}!</h1>

        <section className="section">
          <h2>Nyeste bøger</h2>
          <HomeCardBooks />
        </section>

        {/* Anbefalede bøger og seneste anmeldelser kan forblive som nu */}
      </div>
    </div>
  );
};

export default Home;
