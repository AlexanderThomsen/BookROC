import React, { useState } from "react";
import "./BookCard.css";

const BookCard = ({ book }) => {
  const [favorite, setFavorite] = useState(false);

  return (
    <div className="book-card">
      {/* Billede */}
      <img
        src={book.ImageUrl || "placeholder.png"}
        alt={book.Title}
      />

      {/* Tekst-indhold */}
      <div className="book-content">
        <h3>{book.Title}</h3>
        {book.Author && <p className="author">{book.Author}</p>}
        {book.Description && <p className="description">{book.Description}</p>}
      </div>

      {/* Favorit-knap */}
      <button className="favorite-btn" onClick={() => setFavorite(!favorite)}>
        {favorite ? "⭐" : "☆"} Læs senere
      </button>
    </div>
  );
};

export default BookCard;
