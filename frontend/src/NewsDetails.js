import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import axios from 'axios';
import BaseLayout from './BaseLayout';

const NewsDetails = () => {
  const { id } = useParams();
  const { n } = useParams();
  const [news, setNews] = useState({});
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState({});
  const [group, setGroup] = useState(false);

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

  useEffect(() => {
    const token = localStorage.getItem('token');
    axios
      .get(`http://127.0.0.1:8000/api/news/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(response => {
        setNews(response.data);
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

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <BaseLayout>
      <div className='container'>
        <h2>{news.title}</h2>
        <p><b>Description:</b> {news.description}</p>
        <p><b>Category:</b> {category.title}</p>
        <div className='container text-center'>
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
        <div className='container text-center my-3'>
          {group.includes('Manager') && <Link className="btn btn-primary" to={`/page/${n}/${id}/update`}>Update News</Link>}
        </div>
      </div>
    </BaseLayout>
  );
};

export default NewsDetails;