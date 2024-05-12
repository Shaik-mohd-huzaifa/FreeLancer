import "./App.css";
import { Routes, Route } from "react-router";
import Signins from "./components/Authentication/signins.component";
import Landing from "./components/HomePage/homepage.component";
import Auth from "./components/Authentication/auth.component";
import SelectionComponent from "./components/selection/selection.component";

function App() {
  return (
    <>
      <div className="App">
        <Routes>
          <Route path="/">
            <Route index element={<SelectionComponent />}></Route>
            <Route path="auth">
              <Route index element={<Auth />}></Route>
              <Route path="signin" element={<Signins />}></Route>
            </Route>
          </Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
