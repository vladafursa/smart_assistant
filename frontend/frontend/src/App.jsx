import Home from './pages/Home.jsx';
import Storage from './pages/Storage.jsx';
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
    
return ( 
   <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
           <Route path="/storage" element={<Storage/>} />
        </Routes>
    </BrowserRouter>
)
}

export default App
