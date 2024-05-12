import { useState } from "react";
import axios from "axios";

const FreelancerSide = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("");
  const [cost, setCost] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate the input fields
    if (!name || !email || !skills || !experience || !cost) {
      alert("Please fill in all the fields");
      return;
    }

    try {
      // Create a data object with the user input
      const data = {
        name,
        email,
        skills,
        experience,
        cost,
      };

      const API_URL = "http://localhost:8080/";
      // Send a POST request to the API using Axios
      const response = await axios.post(`${API_URL}freelancerInfo`, data);

      // Handle the response as needed
      console.log(response.data);
    } catch (error) {
      // Handle any errors that occur during the request
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Freelancer Form</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Skills:
          <input
            type="text"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Experience:
          <input
            type="text"
            value={experience}
            onChange={(e) => setExperience(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Cost:
          <input
            type="number"
            value={cost}
            onChange={(e) => setCost(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FreelancerSide;
