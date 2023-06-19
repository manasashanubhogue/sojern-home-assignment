import React from 'react';
import DogImage from './DogImage';

function Favorites() {
  const favorites = JSON.parse(localStorage.getItem('favorites') || '[]');

  return (
    <div className="favorites">
      {favorites.map((image) => (
        <DogImage url={image} />
      ))}
    </div>
  );
}

export default Favorites;