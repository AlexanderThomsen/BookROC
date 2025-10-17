import { Routes, Route, useLocation, Navigate } from 'react-router-dom';
import Header from "./components/Header";
import Footer from "./components/Footer";
import { publicRoutes, privateRoutes } from "./routes/routes.jsx";
import ProtectedRoute from "./components/ProtectedRoute";
import { useAuth } from './context/AuthContext'; // Din auth-context

function AppContent() {
  const { user } = useAuth(); // Antager, at user er null hvis ikke logget ind
  const location = useLocation();
  const isLoginPage = location.pathname === '/login';

  // Redirect logget ind bruger væk fra landing page / login
  if (user && (location.pathname === '/' || isLoginPage)) {
    return <Navigate to="/home" replace />;
  }

  // Tjek om den aktuelle route er en privat route
  const isPrivateRoute = privateRoutes.some(route => route.path === location.pathname);
  
  // Header vises kun hvis: IKKE login page OG IKKE privat route
  const showHeader = !isLoginPage && !isPrivateRoute;

  return (
    <div className="app-wrapper">
      {showHeader && <Header />}

      <main className="landing-wrapper">
        <Routes>
          {/* Public routes */}
          {publicRoutes.map(route => (
            <Route
              key={route.path}
              path={route.path}
              element={route.element}
            />
          ))}

          {/* Private routes */}
          {privateRoutes.map(route => (
            <Route
              key={route.path}
              path={route.path}
              element={<ProtectedRoute>{route.element}</ProtectedRoute>}
            />
          ))}

          {/* Fallback til landing page */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>

      {showHeader && <Footer />}
    </div>
  );
}

export default AppContent;
