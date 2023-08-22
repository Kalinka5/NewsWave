import React, { useState } from 'react';
import axios from 'axios';
import { Navbar, NavDropdown, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const CreateNewsPage = () => {
    const [newTitle, setNewTitle] = useState('');
    const [newDescription, setNewDescription] = useState('');
    const [newCategory, setNewCategory] = useState('');
    const [newImage, setNewImage] = useState(null);

    const handleCreateNews = () => {
      const token = localStorage.getItem('token');

      if (token) {
        const formData = new FormData();
        console.log('Title:', newTitle);
        formData.append('title', newTitle);
        console.log('Description:', newDescription);
        formData.append('description', newDescription);
        console.log('Category:', newCategory);
        formData.append('category', newCategory);
        console.log('Image:', newImage);
        formData.append('images', newImage);

        axios.post(
          'http://127.0.0.1:8000/api/news', formData, {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'multipart/form-data',
            },
          })
        .then(response => {
          // Handle success if needed
          console.log('News created successfully:', response.data);

          // Reset the form fields
          setNewTitle('');
          setNewDescription('');
          setNewCategory('');
          setNewImage(null);
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
            <div className="container pb-3">
              <div className="row justify-content-center">
                <div className="col-md-6">
                    <div className="card mt-3 shadow">
                      <div className="card-body">
                          <div className="text-center">
                            <h4>Create News</h4>
                          </div>
                          <div className="mb-3">
                            <label htmlFor="title" className="form-label">Title</label>
                            <input type="text" className="form-control" id="title" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} />
                          </div>
                          <div className="mb-3">
                            <label htmlFor="description" className="form-label">Description</label>
                            <textarea className="form-control" id="description" value={newDescription} onChange={(e) => setNewDescription(e.target.value)} rows="3"></textarea>
                          </div>
                          <div className="mb-3">
                            <label htmlFor="category" className="form-label">Category</label>
                            <select class="form-select" id="category" aria-label="Default select example" value={newCategory} onChange={(e) => setNewCategory(e.target.value)}>
                              <option selected>Choose News Category</option>
                              <option value="1">Important</option>
                              <option value="4">World</option>
                              <option value="3">Sport</option>
                              <option value="2">Games</option>
                              <option value="7">Fashion</option>
                            </select>
                          </div>
                          <div className="mb-3">
                            <label htmlFor="image" className="form-label">Image</label>
                            <input className="form-control" type="file" id="image" onChange={(e) => setNewImage(e.target.files[0])}></input>
                          </div>
                          <div className="container text-left">
                            <div className="row">
                              <div className="col-auto">
                                <button className="btn btn-primary" onClick={handleCreateNews}>Create</button>
                              </div>
                            </div>
                          </div>
                        </div>
                    </div>
                  </div>
                </div>
              </div>
          </div>
          );
};

export default CreateNewsPage;