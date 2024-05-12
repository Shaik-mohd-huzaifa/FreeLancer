import axios from "axios";
import { createContext, useEffect, useState } from "react";

// Create the user context
export const UserContext = createContext({
  user: null,
  updateUser: () => null,
});

// Create the user context provider component
// eslint-disable-next-line react/prop-types
export const UserProvider = ({ children }) => {
  // State to store the user data
  const [user, updateUser] = useState({ name: "Guest" });

  useEffect(() => {
    axios
      .get("http://localhost:8080/currentUser")
      .then((response) => {
        updateUser(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const value = {
    user,
    updateUser,
  };

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};
