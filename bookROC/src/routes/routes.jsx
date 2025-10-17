import LoginPage from "../pages/LoginPage";
import Home from "../pages/Home";
import LandingPage from "../components/LandingPage";

// Public routes
export const publicRoutes = [
  { path: "/", element: <LandingPage />, hideHeader: false },
  { path: "/login", element: <LoginPage />, hideHeader: true },
];

// Private routes
export const privateRoutes = [
  { path: "/home", element: <Home />, hideHeader: true },
];
