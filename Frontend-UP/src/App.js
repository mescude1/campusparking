import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Profile from "./views/Profile";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </Router>
  );
}

export default App;
