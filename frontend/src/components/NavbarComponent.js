import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import logo from "../images/logo.png";
import { FaArrowAltCircleDown, FaArrowAltCircleUp } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
function NavbarComponent() {
  const navigate = useNavigate();

  function moveToTop() {
    window.scrollTo(0, 0);
  }

  function moveToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
  }
  // function logout(){
  //   localStorage.clear();
  //   navigate("/signup");
  //   window.location.reload()
  // }
  return (
    <Navbar expand="lg" className="fixed-top">
      <Container>
        <Navbar.Brand href="/">
          <img src={logo} width="100px" height="25px" />
        </Navbar.Brand>
        <div className="app">
          <a onClick={moveToTop} className="icon m-2">
            <FaArrowAltCircleUp />
          </a>
        </div>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/recommend">Recommend</Nav.Link>
            <Nav.Link href="/about">About</Nav.Link>
            <Nav.Link href="/contact">Contact</Nav.Link>
            {/* {localStorage.getItem("email") ? <><Nav.Link onClick={logout}>Logout</Nav.Link></> : <><Nav.Link href="/signup">Sign Up</Nav.Link>
            <Nav.Link href="/login">Login</Nav.Link></>} */}
          </Nav>
        </Navbar.Collapse>
        <div className="app">
          <a onClick={moveToBottom} className="icon">
            <FaArrowAltCircleDown />
          </a>
        </div>
      </Container>
    </Navbar>
  );
}

export default NavbarComponent;
