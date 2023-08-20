import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate

  const handleRegister = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/register', {
        username,
        email,
        password,
        first_name,
        last_name,
      });
      setMessage(response.data.message);
      navigate('/login');
    } catch (error) {
      setMessage('An error occurred during registration.');
    }
  };

  return (
    <div className="container position-absolute top-50 start-50 translate-middle">
      <div className="row justify-content-center mt-5">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h1 className="card-title text-center">Register</h1>
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
                  type="email"
                  className="form-control"
                  placeholder="Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
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
              <div className="mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="First name"
                  value={first_name}
                  onChange={(e) => setFirstName(e.target.value)}
                />
              </div>
              <div className="mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Last name"
                  value={last_name}
                  onChange={(e) => setLastName(e.target.value)}
                />
              </div>
              <button className="btn btn-primary float-end" onClick={handleRegister}>
                Register
              </button>
              {message && <p className="mt-2">{message}</p>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;