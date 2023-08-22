import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Navbar, NavDropdown, Nav } from 'react-bootstrap';
import { Link, useParams } from 'react-router-dom';

const NewsPage = ({ user }) => {
  {/* const [isManager, setIsManager] = useState(false); */}
  const { n } = useParams();
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  
  {/* useEffect(() => {
    if (user) {
      // Check if the user is in the "Manager" group
      const isUserManager = user.groups.includes('Manager');
      setIsManager(isUserManager);
    }
  }, [user]);
  */}
  useEffect(() => {
    const token = localStorage.getItem('token'); // Get the token from local storage

    if (token) {
      // Include the token in the headers of the GET request
      axios.get(`http://127.0.0.1:8000/api/news?page=${n}`, {
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
  }, [n]);

    if (loading) {
      return <p>Loading...</p>;
    }

    return (
        <div className="container mt-5">
            <Navbar bg="light" expand="lg">
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
                      <Link className="page-link" to="/create-news">Create News</Link>
                      {/* {isManager && <Link className="page-link" to="/create-news">Create News</Link>}*/}
                    </Nav>
                </Navbar.Collapse>
                <nav aria-label="Page navigation example">
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
                            <Link to={`/page/${n}/${item.id}`} className="btn btn-primary">
                              Read More
                            </Link>
                        </div>
                    </div>
                </div>
                ))}
            </div>
          </div>
          );
};

export default NewsPage;