import React from 'react';

function DogImage({ url }) {
  const handleFavorite = () => {
    const favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    if (!favorites.includes(url)) {
      favorites.push(url);
      localStorage.setItem('favorites', JSON.stringify(favorites));
    }
  };

  return (
    <div className="dog-image">
      <img width="400" src={url} alt="Dog" />
      <button onClick={handleFavorite}>Favorite</button>
    </div>
  );
}

export default DogImage;