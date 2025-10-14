// Pages import
import LoginPage from "../pages/LoginPage";
import Home from "../pages/Home";
import LandingPage from "../components/LandingPage";
// Du kan senere importere flere private sider her

// Public routes
export const publicRoutes = [
  { 
    path: "/", 
    element: <LandingPage />,
    hideHeader: false 
  },
  { 
    path: "/login", 
    element: <LoginPage />,
    hideHeader: true 
  },
];

// Private routes (tom indtil videre)
export const privateRoutes = [
  { 
    path: "/home", 
    element: <Home />,
    hideHeader: true 
  },
];