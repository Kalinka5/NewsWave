import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import BaseLayout from './BaseLayout';

const UpdateNews = () => {
  const { id } = useParams();
  const { n } = useParams();
  const [news, setNews] = useState({});
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState({});

  const [newTitle, setNewTitle] = useState(news.title);
  const [newDescription, setNewDescription] = useState(news.description);
  const [newCategory, setNewCategory] = useState(category.id);
  const [newImage, setNewImage] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    axios
      .get(`http://127.0.0.1:8000/api/news/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(response => {
        const fetchedNews = response.data;
        setNews(fetchedNews);
        setNewTitle(fetchedNews.title);
        setNewDescription(fetchedNews.description);
        setNewCategory(fetchedNews.category)
        setLoading(false);
        // Fetch category information
        axios
          .get(`http://127.0.0.1:8000/api/categories/${response.data.category}`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          })
          .then(categoryResponse => {
            setCategory(categoryResponse.data);
          })
          .catch(categoryError => {
            console.error('Error fetching category:', categoryError);
          });
      })
      .catch(error => {
        console.error('Error fetching news details:', error);
        setLoading(false);
      });
  }, [id]);

  const handleAddImage = () => {
    const token = localStorage.getItem('token');

    if (token) {
        const formData = new FormData();
        console.log('Image:', newImage);
        formData.append('images', newImage);

        axios.patch(
            `http://127.0.0.1:8000/api/news/${id}`, formData, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        )
        .then(response => {
            console.log('News updated successfully:', response.data);
            navigate(`/page/${n}/${id}`);
        })
        .catch(error => {
            console.error('Error updating news:', error);
        });
        } else {
        console.log('Token not found in local storage. User is not authenticated.');
        }
    };

  const handleUpdateNews = () => {
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

        axios.put(
            `http://127.0.0.1:8000/api/news/${id}`, formData, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        )
        .then(response => {
            console.log('News updated successfully:', response.data);
            navigate(`/page/${n}/${id}`);
        })
        .catch(error => {
            console.error('Error updating news:', error);
        });
        } else {
        console.log('Token not found in local storage. User is not authenticated.');
        }
    };

  const handleDeleteNews = () => {
    const token = localStorage.getItem('token');

    if (token) {
      axios.delete(`http://127.0.0.1:8000/api/news/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(response => {
        console.log('News deleted successfully:', response.data);
        // Redirect the user to the news page
        navigate('/page/1');
      })
      .catch(error => {
        console.error('Error deleting news:', error);
      });
    } else {
      console.log('Token not found in local storage. User is not authenticated.');
    }
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <BaseLayout>
      <div className='container pt-3'>
        <div className="mb-3">
            <label htmlFor="title" className="form-label"><b>Title:</b></label>
            <input type="text" className="form-control" id="title" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} />
        </div>
        <div className="mb-3">
            <label htmlFor="description" className="form-label"><b>Description:</b></label>
            <textarea className="form-control" id="description" value={newDescription} onChange={(e) => setNewDescription(e.target.value)} rows="5"></textarea>
        </div>
        <div className="mb-3">
            <label htmlFor="category" className="form-label"><b>Category:</b></label>
            <select className="form-select" id="category" aria-label="Default select example" value={newCategory} onChange={(e) => setNewCategory(e.target.value)}>
                <option >Choose News Category</option>
                <option value="1">Important</option>
                <option value="4">World</option>
                <option value="3">Sport</option>
                <option value="2">Games</option>
                <option value="7">Fashion</option>
            </select>
        </div>
        <div className="mb-3">
            <label htmlFor="image" className="form-label"><b>Image:</b></label>
            <input className="form-control" type="file" id="image" onChange={(e) => setNewImage(e.target.files[0])}></input>
        </div>
        <div className='container text-left ps-0'>
        {news.images?.map((image, index) => (
          <img
            key={index}
            src={`http://127.0.0.1:8000${image.image}`}
            alt={`News ${index + 1}`}
            className="me-3 mb-3"
            width={`300px`}
          />
        ))}
        </div>
        <div className='container my-3 ps-0'>
          <div class="row justify-content-between">
            <div class="col-4">
              <button type="button" className="btn btn-outline-primary me-3" onClick={handleAddImage}>Add image</button>
              <button type="button" className="btn btn-outline-secondary me-3" onClick={handleUpdateNews}>Update News</button>
            </div>
            <div class="col-4 text-center">
              <button type="button" className="btn btn-outline-danger" onClick={handleDeleteNews}>Delete News</button>
            </div>
          </div>
        </div>
      </div>
    </BaseLayout>
  );
};

export default UpdateNews;