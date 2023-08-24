import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import BaseLayout from './BaseLayout';

const CategoryNews = () => {
    const { title } = useParams();
    const [news, setNews] = useState([]);
    const [loading, setLoading] = useState(true);
  
    useEffect(() => {
      const token = localStorage.getItem('token'); // Get the token from local storage
  
      if (token) {
        // Include the token in the headers of the GET request
        axios.get(`http://127.0.0.1:8000/api/news?category=${title}`, {
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
    }, [title]);

    if (loading) {
        return <p>Loading...</p>;
      }

    return (
        <BaseLayout>
            <div className='container pt-3'>
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
                            <button className="btn btn-primary">Read More</button>
                        </div>
                    </div>
                </div>
                ))}
            </div>
            </div>
        </BaseLayout>
        );
};

export default CategoryNews;