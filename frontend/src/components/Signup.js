import { useNavigate } from "react-router-dom";
import React, { useState, useEffect } from "react";
// import back from "./my-account.jpg";
// import "./login.css";
export default function Signup(props) {
  const navigate = useNavigate();
  const [username, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const[confirmPassword,setConfirmPassword] = useState("");
  useEffect(() => {
    localStorage.clear();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = "http://127.0.0.1:8000/api/register/";
    const data = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: e.target.username.value,
        email: e.target.email.value,
        password: e.target.password.value,
        confirm_password : e.target.confirm_password.value,
      }),
    });
    const response = await data.json();
    console.log(response)
    if (response) {
      
      props.showAlert("User Signed in Successfully", "success");
      navigate("/login");
      localStorage.setItem("email",email);
    } else {
      props.showAlert(response.error || "User registration failed!User Already exists", "danger");
    }
  };

  return (
    <>
      <section className="login">
        <div className="container">
          <div className="backImg">
            {/* <img src={back} alt="" /> */}
            <div className="text">
              <h3>Register</h3>
              <h1>My account</h1>
            </div>
          </div>

          <form method="post" onSubmit={handleSubmit}>
            <span>Username *</span>
            <input
              type="text"
              className="form-control"
              id="username"
              name="username"
              value={username}
              onChange={(e) => {
                setName(e.target.value);
              }}
              required
            />
            <span>Email address *</span>
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              value={email}
              aria-describedby="emailHelp"
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              required
            />

            <span>Password *</span>
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              value={password}
              placeholder="Enter your password"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              required
            />
            <span>Confirm Password *</span>
            <input
              type="password"
              className="form-control"
              id="confirm_password"
              name="confirm_password"
              value={confirmPassword}
              placeholder="Confirm your password"
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />

            <button className="button">Register</button>

          </form>
        </div>
      </section>
    </>
  );
}