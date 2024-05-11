import { UserContext } from "../../contexts/user.context";
import { useContext } from "react";
const Landing = () => {
  const { user } = useContext(UserContext);
  return (
    <div className="">
      <p>{user.name || "None"}</p>
    </div>
  );
};

export default Landing;
