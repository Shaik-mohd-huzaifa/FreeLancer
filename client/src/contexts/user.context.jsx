import { createContext, useState } from "react";

// Create the user context
export const UserContext = createContext({
  user: null,
  updateUser: () => {},
});

// Create the user context provider component
// eslint-disable-next-line react/prop-types
export const UserProvider = ({ children }) => {
  // State to store the user data
  const [user, setUser] = useState({});

  // Function to update the user data
  const updateUser = (userData) => {
    setUser(userData);
  };

  // Value object to be provided by the context
  const value = {
    user,
    updateUser,
  };

  // Render the context provider with the provided value
  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};
