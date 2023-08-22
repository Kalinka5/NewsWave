import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/', {
        username,
        password,
      });
      const token = response.data.access;
      localStorage.setItem('token', token);
      setErrorMessage('');
  
      // Redirect the user to the news page
      navigate('/page/1');
    } catch (error) {
      setErrorMessage('Invalid credentials. Please try again.');
    }
  };

  return (
    <div className="container position-absolute top-50 start-50 translate-middle">
      <div className="row justify-content-center mt-5">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h1 className="card-title text-center">Login</h1>
              <div className="mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </div>
              <div className="mb-3">
                <input
                  type="password"
                  className="form-control"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
              <button className="btn btn-primary float-end" onClick={handleLogin}>
                Login
              </button>
              {errorMessage && <p className="text-danger mt-2">{errorMessage}</p>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;