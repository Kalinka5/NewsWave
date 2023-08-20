import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import NewsPage1 from './NewsPage1';
import NewsPage2 from './NewsPage2';
import CategoryNews from './CategoryNews';
import NewsDetails from './NewsDetails';

ReactDOM.render(<RootApp />, document.getElementById('root'));

function RootApp() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/page1" element={<NewsPage1 />} />
        <Route path="/page1/:id" element={<NewsDetails />} />
        <Route path="/page2" element={<NewsPage2 />} />
        <Route path="/category/:title" element={<CategoryNews />} />
      </Routes>
    </Router>
  );
}

export default App;