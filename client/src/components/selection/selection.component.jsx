import { useState } from "react";
import FreelancerSide from "./freelancerside";
import ClientSide from "./ClientSide";

const SelectionComponent = () => {
  const [isFreelancer, setIsFreelancer] = useState(true);

  const handleSwitchComponent = () => {
    setIsFreelancer(!isFreelancer);
  };

  return (
    <div>
      <h1>Selection Component</h1>
      {isFreelancer ? <FreelancerSide /> : <ClientSide />}
      <button onClick={handleSwitchComponent}>
        {isFreelancer ? "Switch to Client" : "Switch to Freelancer"}
      </button>
    </div>
  );
};

export default SelectionComponent;
