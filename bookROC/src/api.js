const API_BASE = "http://127.0.0.1:8000"; // FastAPI backend

export async function fetchBooks() {
  const res = await fetch(`${API_BASE}/books/books`);
  if (!res.ok) throw new Error("Failed to fetch books");
  return await res.json();
}
