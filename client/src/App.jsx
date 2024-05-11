import "./App.css";
import { Routes, Route } from "react-router";
import Signins from "./components/Authentication/signins.component";
import Landing from "./components/HomePage/homepage.component";
import Auth from "./components/Authentication/auth.component";
import { UserProvider } from "./contexts/user.context";
function App() {
  return (
    <>
      <UserProvider>
        <div className="App">
          <Routes>
            <Route path="/">
              <Route index element={<Landing />}></Route>
              <Route path="auth">
                <Route index element={<Auth />}></Route>
                <Route path="signin" element={<Signins />}></Route>
              </Route>
            </Route>
          </Routes>
        </div>
      </UserProvider>
    </>
  );
}

export default App;
