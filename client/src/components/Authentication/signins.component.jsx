import axios from "axios";
import { UserContext } from "../../contexts/user.context";
import { useContext } from "react";

const Signins = () => {
  const { updateUser } = useContext(UserContext);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const name = event.target.name.value;
    const email = event.target.email.value;
    const password = event.target.password.value;

    try {
      const response = await axios.post("http://localhost:8080/api/signin", {
        name,
        email,
        password,
      });
      updateUser(response.data);
      console.log(response.data);

      // Handle success
    } catch (error) {
      console.error(error);
      // Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign Up</h2>
      <label htmlFor="name">Name</label>
      <input type="text" id="name" name="name" required />
      <label htmlFor="email">Email</label>
      <input type="email" id="email" name="email" required />
      <label htmlFor="password">Password</label>
      <input type="password" id="password" name="password" required />
      <button type="submit">Sign Up</button>
    </form>
  );
};

export default Signins;
