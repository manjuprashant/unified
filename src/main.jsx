import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";
import "./App.css";

import keycloak from "./keycloak";


keycloak
  .init({
    onLoad: "login-required",
    checkLoginIframe: false
  })
  .then((authenticated) => {

    if (!authenticated) {

      console.log("User not authenticated");

      return;
    }

    localStorage.setItem(
      "access_token",
      keycloak.token
    );

    ReactDOM.createRoot(
      document.getElementById("root")
    ).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );

  })
  .catch((error) => {

    console.error(
      "Keycloak initialization failed",
      error
    );

  });