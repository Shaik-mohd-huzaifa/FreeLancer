import { useState } from "react";
import axios from "axios";

const ClientSide = () => {
  const [formData, setFormData] = useState({
    project_name: "",
    project_id: "",
    client_country: "",
    client_state: "",
    summary: "",
    technologies: "",
  });
  const [responseData, setResponseData] = useState(null); // Add state for response data

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:8080/freelancerInfo",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        },
      );

      setResponseData(response.data); // Store the response data in state
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Client Name:
          <input
            type="text"
            name="client_name"
            value={formData.client_name}
            onChange={handleChange}
          />
        </label>
        <label>
          Client Country:
          <input
            type="text"
            name="client_country"
            value={formData.client_country}
            onChange={handleChange}
          />
        </label>
        <label>
          Summary:
          <textarea
            name="summary"
            value={formData.summary}
            onChange={handleChange}
          />
        </label>
        <label>
          Skills Required:
          <input
            type="text"
            name="skills_required"
            value={formData.skills_required}
            onChange={handleChange}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
      {responseData && (
        <div>
          <h2>Response Data:</h2>
          <pre>{JSON.stringify(responseData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default ClientSide;
