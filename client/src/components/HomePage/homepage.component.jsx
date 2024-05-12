import { UserContext } from "../../contexts/user.context";
import { useContext, useEffect, useState } from "react";
const Landing = () => {
  const { user } = useContext(UserContext);
  return (
    <div className="">
      <p>{user.name || "Guest"}</p>
    </div>
  );
};

export default Landing;
