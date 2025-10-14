import { Routes, Route, useLocation } from 'react-router-dom';
import Header from "./components/Header";
import Footer from "./components/Footer";
import { publicRoutes, privateRoutes } from "./routes/routes.jsx";
import ProtectedRoute from "./components/ProtectedRoute";

function AppContent() {
  const location = useLocation();
  const isLoginPage = location.pathname === '/login';
  
  // Tjek om den aktuelle route er en privat route
  const isPrivateRoute = privateRoutes.some(route => route.path === location.pathname);
  
  // Header vises kun hvis: IKKE login page OG IKKE privat route
  const showHeader = !isLoginPage && !isPrivateRoute;

  return (
    <div className="app-wrapper">
      {showHeader && <Header />}

      <main className="landing-wrapper">
        <Routes>
          {publicRoutes.map(route => (
            <Route key={route.path} path={route.path} element={route.element} />
          ))}

          {privateRoutes.map(route => (
            <Route
              key={route.path}
              path={route.path}
              element={<ProtectedRoute>{route.element}</ProtectedRoute>}
            />
          ))}

          {/* Fallback til login */}
          <Route path="*" element={publicRoutes[0].element} />
        </Routes>
      </main>

      {showHeader && <Footer />}
    </div>
  );
}

export default AppContent;