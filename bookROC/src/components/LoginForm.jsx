import { useState } from 'react';
import { useNavigate } from 'react-router-dom';  // 👈 Tilføj denne
import { GoogleLogin } from '@react-oauth/google';
import './LoginForm.css';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // 👈 Opret navigate hook

  // Normal login
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login med', email, password);
  };

  // Google login
  const handleGoogleSuccess = async (credentialResponse) => {
    const googleToken = credentialResponse.credential;

    try {
      const response = await fetch('http://127.0.0.1:8000/auth/google', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: googleToken }),
      });

      const data = await response.json();

      if (data.user && data.access_token) {
        console.log('Bruger verificeret af backend:', data.user);
        localStorage.setItem('user', JSON.stringify(data.user));
        localStorage.setItem('token', data.access_token); // brug backend JWT
        navigate("/home"); // 👉 sender brugeren til Home
      } else {
        alert('Login fejlede');
      }
    } catch (error) {
      console.error('Fejl:', error);
      alert('Login fejlede');
    }
  };

  const handleGoogleError = () => {
    console.log('Google login fejlede');
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
    <h2>Login</h2>

    <input
      type="email"
      placeholder="Email"
      value={email}
      onChange={(e) => setEmail(e.target.value)}
      required
    />

    <input
      type="password"
      placeholder="Password"
      value={password}
      onChange={(e) => setPassword(e.target.value)}
      required
    />

    <button type="submit">Login</button>

    <div className="google-login">
      <GoogleLogin onSuccess={handleGoogleSuccess} onError={handleGoogleError} />
    </div>

    <div className="login-links">
      <button type="button">Glemt adgangskode?</button>
    </div>

    <div className="form-footer">
      <p>Har du ikke en bruger?</p>
      <button type="button">Tilmeld dig her</button>
    </div>
  </form>
  );
}
