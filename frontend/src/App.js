import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Login from './Login';
import Register from './Register';
import NewsPage from './NewsPage';
import CreateNewsPage from './CreateNews';
import CategoryNews from './CategoryNews';
import NewsDetails from './NewsDetails';
import UpdateNews from './UpdateNews';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/page/:n" element={<NewsPage />} />
        <Route path="/create-news" element={<CreateNewsPage />} />
        <Route path="/page/:n/:id" element={<NewsDetails />} />
        <Route path="/page/:n/:id/update" element={<UpdateNews />} />
        <Route path="/category/:title" element={<CategoryNews />} />
      </Routes>
    </Router>
  );
}

export default App;