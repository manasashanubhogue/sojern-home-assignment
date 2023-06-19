import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Gallery from './components/Gallery';
import Favorites from './components/Favorites';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/favorites">Favorites</Link>
          </li>
        </ul>
      </nav>
      <Switch>
        <Route exact path="/">
          <Gallery />
        </Route>
        <Route path="/favorites">
          <Favorites />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;