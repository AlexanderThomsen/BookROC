import React, { useEffect, useState, useRef } from "react";
import BookCard from "./BookCard";
import { fetchBooks } from "../api";
import "./HomeCardBooks.css";

const HomeCardBooks = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const scrollRef = useRef(null);

  useEffect(() => {
    fetchBooks()
      .then(setBooks)
      .catch(err => console.error("Kunne ikke hente bøger:", err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;

  const scroll = (direction) => {
    if (scrollRef.current) {
      const scrollAmount = 240; // bredden på et kort + margin
      scrollRef.current.scrollBy({
        left: direction === "left" ? -scrollAmount : scrollAmount,
        behavior: "smooth",
      });
    }
  };

  return (
    <div className="carousel-container">
      <button className="scroll-btn left" onClick={() => scroll("left")}>◀</button>
      <div className="books-grid" ref={scrollRef}>
        {books.slice(0, 10).map(book => (
          <BookCard key={book.BookID} book={book} />
        ))}
      </div>
      <button className="scroll-btn right" onClick={() => scroll("right")}>▶</button>
    </div>
  );
};

export default HomeCardBooks;
