import React, { useState } from "react";


function App() {

  const [applications, setApplications] = useState({
    jira: true,
    github: true,
    slack: true
  });


  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);


  function toggleApplication(application) {

    setApplications({

      ...applications,

      [application]:
        !applications[application]

    });

  }


  async function provisionUser() {

    setLoading(true);

    setResult(null);


    try {

      const selectedApplications =
        Object.keys(applications)
          .filter(
            app => applications[app]
          );


      const token =
        localStorage.getItem(
          "access_token"
        );


      const response = await fetch(
        "http://localhost:8000/api/users/provision",
        {

          method: "POST",

          headers: {

            "Content-Type":
              "application/json",

            "Authorization":
              `Bearer ${token}`

          },

          body: JSON.stringify({

            applications:
              selectedApplications

          })

        }
      );


      const data = await response.json();

      setResult(data);


    } catch (error) {

      setResult({
        error: error.message
      });

    }


    setLoading(false);

  }


  return (

    <div className="container">

      <h1>
        Unified User Provisioning
      </h1>


      <p>
        Create your account across
        multiple applications.
      </p>


      <div className="card">

        <h2>
          Select Applications
        </h2>


        <label>

          <input
            type="checkbox"
            checked={applications.jira}
            onChange={() =>
              toggleApplication("jira")
            }
          />

          Jira

        </label>


        <label>

          <input
            type="checkbox"
            checked={applications.github}
            onChange={() =>
              toggleApplication("github")
            }
          />

          GitHub

        </label>


        <label>

          <input
            type="checkbox"
            checked={applications.slack}
            onChange={() =>
              toggleApplication("slack")
            }
          />

          Slack

        </label>


        <button
          onClick={provisionUser}
          disabled={loading}
        >

          {loading
            ? "Creating..."
            : "Create User Accounts"}

        </button>


      </div>


      {result && (

        <div className="result">

          <h2>
            Provisioning Result
          </h2>

          <pre>
            {JSON.stringify(
              result,
              null,
              2
            )}
          </pre>

        </div>

      )}

    </div>

  );

}


export default App;