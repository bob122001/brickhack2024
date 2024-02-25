import logo from './images/logo.svg';
import './App.css';

function App() {
  
  //no real functionality, this is just putting some color stuff in and whatnot
  
  return (
    <div className="App-page">
      <div className="App-form-container">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          This is going to be a nice sentence to test out some fonts on our background color to check the readability. This is gonna be important! Woohoo!!
        </p>
      </div>
    </div>
  );
}

export default App;
