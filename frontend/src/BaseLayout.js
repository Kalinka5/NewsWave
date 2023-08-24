import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Navbar, NavDropdown, Nav } from 'react-bootstrap';

const BaseLayout = ({ children }) => {
  const [group, setGroup] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');

    if (token) {
      // Include the token in the headers of the GET request
      axios.get(`http://127.0.0.1:8000/api/current-user/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(response => {
        setGroup(response.data.groups);
      })
      .catch(error => {
        console.error('Error fetching news:', error);
      });
    } else {
      console.log('Token not found in local storage. User is not authenticated.');
    }
  }, []);

  return (
    <div className="container mt-5">
      {/* Your common header content */}
      <header>
        <Navbar bg="light" expand="lg">
            <div className="container-fluid">
                <Navbar.Brand><Link className="page-link" to="/page/1">News</Link></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <NavDropdown title="Category" id="basic-nav-dropdown">
                            <NavDropdown.Item><Link className="page-link" to="/category/Important">Important</Link></NavDropdown.Item>
                            <NavDropdown.Item><Link className="page-link" to="/category/World">World</Link></NavDropdown.Item>
                            <NavDropdown.Item><Link className="page-link" to="/category/Sport">Sport</Link></NavDropdown.Item>
                            <NavDropdown.Item><Link className="page-link" to="/category/Games">Games</Link></NavDropdown.Item>
                            <NavDropdown.Item><Link className="page-link" to="/category/Fashion">Fashion</Link></NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                    <Nav className="me-auto">
                      {group.includes('Manager') && <Link className="btn btn-outline-info" to="/create-news">Create News</Link>}
                    </Nav>
                </Navbar.Collapse>
                <nav aria-label="Page navigation example" className='pt-3'>
                    <ul className="pagination">
                    <li className="page-item">
                    <Link className="page-link" to="#">
                        <span aria-hidden="true">&laquo;</span>
                    </Link>
                    </li>
                    <li className="page-item"><Link className="page-link" to="/page/1">1</Link></li>
                    <li className="page-item"><Link className="page-link" to="/page/2">2</Link></li>
                    <li className="page-item">
                        <Link className="page-link" to="#">
                            <span aria-hidden="true">&raquo;</span>
                        </Link>
                    </li>
                    </ul>
                </nav>
            </div>
        </Navbar>
      </header>

      {/* Content specific to each page */}
      <main>
        {children}
      </main>

    </div>
  );
};

export default BaseLayout;