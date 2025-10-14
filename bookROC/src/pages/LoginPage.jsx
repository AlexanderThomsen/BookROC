import LoginForm from '../components/LoginForm';
import './LoginPage.css';

export default function LoginPage() {
  return (
    <div className="login-page-wrapper">
      <div className="login-illustration">
        <h1>her kan være noget illustration</h1>
      </div>

      <div className="login-form-container">
        <LoginForm />
      </div>
    </div>
  );
}
