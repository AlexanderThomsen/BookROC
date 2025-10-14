import React, { useEffect, useState } from "react";
import Sidebar from "../components/sidebar";
import "./Home.css";

const Home = ({ userId }) => { // userId sendes fra login/session
  const [userName, setUserName] = useState("");

  useEffect(() => {
    if (!userId) return;

    fetch(`/api/users/${userId}`) // Dit FastAPI endpoint
      .then((res) => res.json())
      .then((data) => {
        setUserName(data.username); // data.username fra UserRead
      })
      .catch((err) => console.error("Kunne ikke hente bruger:", err));
  }, [userId]);

  const latestBooks = [
    { title: "1984", author: "George Orwell" },
    { title: "Brave New World", author: "Aldous Huxley" },
    { title: "Fahrenheit 451", author: "Ray Bradbury" },
  ];

  const recommendedBooks = [
    { title: "The Hobbit", author: "J.R.R. Tolkien" },
    { title: "Dune", author: "Frank Herbert" },
  ];

  const recentReviews = [
    { user: "Anna", book: "1984", review: "Fremragende bog!" },
    { user: "Mark", book: "Dune", review: "En episk rejse gennem universet." },
  ];

  return (
    <div className="home-container">
      <Sidebar />
      <div className="home-main">
        <h1>Velkommen {userName ? userName : "til BookROC"}!</h1>

        <section className="section">
          <h2>Nyeste bøger</h2>
          <ul>
            {latestBooks.map((book, index) => (
              <li key={index}>
                <strong>{book.title}</strong> af {book.author}
              </li>
            ))}
          </ul>
        </section>

        <section className="section">
          <h2>Anbefalede bøger</h2>
          <ul>
            {recommendedBooks.map((book, index) => (
              <li key={index}>
                <strong>{book.title}</strong> af {book.author}
              </li>
            ))}
          </ul>
        </section>

        <section className="section">
          <h2>Seneste anmeldelser</h2>
          <ul>
            {recentReviews.map((review, index) => (
              <li key={index}>
                <strong>{review.user}</strong> på <em>{review.book}</em>: "{review.review}"
              </li>
            ))}
          </ul>
        </section>
      </div>
    </div>
  );
};

export default Home;
