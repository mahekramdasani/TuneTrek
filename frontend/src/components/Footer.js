import React from "react";
import footer from '../images/footer.png'
import {TfiInstagram,TfiEmail} from 'react-icons/tfi'
import {RiTwitterXLine} from 'react-icons/ri'
import {BsLinkedin} from 'react-icons/bs'
const Footer = () => {
  return (
    <>
      <div className="row footer">
        <div className="container img">
          <img src={footer} width="250px" height="100px" className="footer-logo"/>
        </div>
        <div className="col-lg-4">
          <h3>SITEMAP</h3>
          <ul type="none">
            <li>
              <a href="./" className="footer-link">Home</a>
            </li>
            <li>
              <a href="./recommend" className="footer-link">Recommend</a>
            </li>
            <li>
              <a href="./about" className="footer-link">About</a>
            </li>
            <li>
              <a href="./contact" className="footer-link">Contact</a>
            </li>
            <li>
              <a href="./login" className="footer-link">Login</a>
            </li>
            <li>
              <a href="./signup" className="footer-link">Sign Up</a>
            </li>
            <li>
              <a href="./faq" className="footer-link">FAQ</a>
            </li>
          </ul>
        </div>
        <div className="col-lg-4">
          <h3>Our Mission and Goals</h3>
          <p className="footer-body">
            At our website TuneTrek, our mission is to revolutionize music discovery by providing personalized recommendations and fostering a vibrant community of music enthusiasts.
          </p>
        </div>
        <div className="col-lg-4">
          <h3>FEEL FREE TO CONNECT WITH US</h3>
          <ul type="none">
            <li>
            <a href="https://www.instagram.com" className="footer-link">
                <TfiInstagram className="icon"/><span className="m-1">tunetrek</span>
              </a>
            </li>
            <li>
            <a href="https://www.twitter.com" className="footer-link">
                <RiTwitterXLine className="icon"/><span className="m-1">tunetrek</span>
              </a>
            </li>
            <li>
            <a href="https://www.linkedin.com" className="footer-link">
                <BsLinkedin className="icon"/><span className="m-1">tunetrek</span>
              </a>
            </li>
            <li>
            <a href="https://www.gmail.com" className="footer-link">
                <TfiEmail className="icon"/><span className="m-1">trek</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default Footer;