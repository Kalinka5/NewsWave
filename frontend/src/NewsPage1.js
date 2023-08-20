import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Navbar, NavDropdown, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const NewsPage = () => {
    const [news, setNews] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      const token = localStorage.getItem('token'); // Get the token from local storage
  
      if (token) {
        // Include the token in the headers of the GET request
        axios.get('http://127.0.0.1:8000/api/news?page=1', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(response => {
          setNews(response.data);
          setLoading(false);
        })
        .catch(error => {
          console.error('Error fetching news:', error);
          setLoading(false);
        });
      } else {
        console.log('Token not found in local storage. User is not authenticated.');
        setLoading(false);
      }
    }, []);
    
    const [newTitle, setNewTitle] = useState('');
    const [newDescription, setNewDescription] = useState('');
    const [newCategory, setNewCategory] = useState('');
    const [newImage, setNewImage] = useState('');

    const handleCreateNews = () => {
      const token = localStorage.getItem('token');

      if (token) {
        axios.post(
          'http://127.0.0.1:8000/api/news/',
          {
            title: newTitle,
            description: newDescription,
            category: newCategory,
            images: newImage,
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        )
        .then(response => {
          // Handle success if needed
          console.log('News created successfully:', response.data);
        })
        .catch(error => {
          // Handle error if needed
          console.error('Error creating news:', error);
        });
      } else {
        console.log('Token not found in local storage. User is not authenticated.');
      }
    };

    return (
        <div className="container mt-5">
            <Navbar bg="light" expand="lg">
              <Navbar.Brand><Link className="page-link" to="/page1">News</Link></Navbar.Brand>
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
                </Navbar.Collapse>
                <nav aria-label="Page navigation example">
                    <ul className="pagination">
                        <li className="page-item">
                        <Link className="page-link" to="#">
                            <span aria-hidden="true">&laquo;</span>
                        </Link>
                        </li>
                        <li className="page-item"><Link className="page-link" to="/page1">1</Link></li>
                        <li className="page-item"><Link className="page-link" to="/page2">2</Link></li>
                        <li className="page-item">
                            <Link className="page-link" to="#">
                                <span aria-hidden="true">&raquo;</span>
                            </Link>
                        </li>
                    </ul>
                </nav>
            </Navbar>
            <br></br>
            <div className="row">
                {news.map(item => (
                <div key={item.id} className="col-md-6 col-lg-4 mb-4">
                    <div className="card">
                        {item.images.length > 0 && (
                            <img className="card-img-top" src={`http://127.0.0.1:8000/${item.images[0].image}`} alt="News"/>
                        )}
                        <div className="card-body">
                            <h5 className="card-title">{item.title}</h5>
                            <p className="card-text">{item.description}</p>
                            <Link to={`/page1/${item.id}`} className="btn btn-primary">
                              Read More
                            </Link>
                        </div>
                    </div>
                </div>
                ))}
            </div>
          {/* Add the card for creating news */}
          <div className="row mt-4">
              <div className="col-md-12">
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">Create News</h5>
                    <div className="mb-3">
                      <label htmlFor="title" className="form-label">Title</label>
                      <input type="text" className="form-control" id="title" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} />
                    </div>
                    {/* Add more fields as needed */}
                    <button className="btn btn-primary" onClick={handleCreateNews}>Create</button>
                  </div>
                </div>
              </div>
            </div>
        </div>
        );
};

export default NewsPage;