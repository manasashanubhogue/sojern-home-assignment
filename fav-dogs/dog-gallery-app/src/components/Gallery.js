import React, { useEffect, useState } from 'react';
import DogImage from './DogImage';
import { fetchRandomDogImages } from '../api';

function Gallery() {
  const [dogImages, setDogImages] = useState([]);

  useEffect(() => {
    fetchImages();
  }, []);

  const fetchImages = async () => {
    try {
      const images = await fetchRandomDogImages();
      setDogImages(images);
    } catch (error) {
      console.error('Error fetching dog images:', error);
    }
  };

  const handleNext = () => {
    fetchImages();
  };
  

  return (
    <div className="gallery">
        <DogImage url={dogImages} />
      <button onClick={handleNext}>NEXT</button>
    </div>
  );
}

export default Gallery;