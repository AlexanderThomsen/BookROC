import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleGoogleLogin = async () => {
    // Her skal du tilføje din Google login logik
    // Dette er bare et eksempel med mock-data:
    const googleUser = {
      id: '123',
      name: 'Alexander Thomsen',
      email: 'alex@example.com',
      token: 'abc123',
    };

    login(googleUser); // Gemmer user i context + localStorage
    navigate('/home'); // Send til privat side
  };

  return (
    <div style={{ padding: 50 }}>
      <h1>Login</h1>
      <button onClick={handleGoogleLogin}>Login med Google</button>
    </div>
  );
};

export default LoginPage;
