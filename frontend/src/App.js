import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import SongList from './components/SongList';
import NavbarComponent from './components/NavbarComponent';
import Footer from './components/Footer';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import Recommend from './components/Recommend';
import Contact from './components/Contact';
import About from './components/About';
import Alert from './components/Alert';
function App() {
  const [alert, setAlert] = useState(null);
  const showAlert = (message, type) => {
    setAlert({
      msg: message,
      type: type,
    });
    setTimeout(() => {
      setAlert(null);
    }, 1500);
  };

  
  return (
    <>
    <BrowserRouter>
    <NavbarComponent/>
    <main>
    <Alert alert={alert} />
    <Routes>
      <Route path="/" element = {<SongList showAlert = {showAlert}/>}/>
      <Route path="/about" element = {<About showAlert = {showAlert}/>}/>
      <Route path="/recommend" element = {<Recommend showAlert = {showAlert}/>}/>
      <Route path="/contact" element={<Contact showAlert = {showAlert}/>} />
      <Route path = "/signup" element={<Signup showAlert = {showAlert}/>}/>
      <Route path="/login" element={<Login showAlert = {showAlert}/>}/>
      </Routes>
    </main>
    </BrowserRouter>

    <Footer/>
    
    </>
  );
}

export default App;
