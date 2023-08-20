import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const NewsDetails = () => {
  const { id } = useParams();
  const [news, setNews] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token'); // Get the token from local storage
    axios.get(`http://127.0.0.1:8000/api/news/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(response => {
        setNews(response.data);
        setLoading(false);
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
    <div className="container mt-5">
      <h1>{news.title}</h1>
      <p>{news.description}</p>
      <p>Category: {news.category?.title}</p>
      {news.images?.map((image, index) => (
        <img
          key={index}
          src={`http://127.0.0.1:8000${image.image}`}
          alt={`News ${index + 1}`}
          width={`300px`}
        />
      ))}
    </div>
  );
};

export default NewsDetails;