import React, { useEffect, useState } from "react";
import HomeHeader from "../components/HomeHeader";
import "./Home.css";
import HomePage from '../components/HomePage';

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
        <HomeHeader />
        <div className="home-main">
          <HomePage />
        </div>
      </div>
  );
};

export default Home;
