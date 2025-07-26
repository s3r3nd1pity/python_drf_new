import {useEffect, useState} from "react";
import axios from "axios";

function App() {
    const [pizzas, setPizzas] = useState([])
    useEffect(() => {
        axios.get('/api')
    }, []);
  return (
    <div className="App">
      <div>App</div>
    </div>
  );
}

export default App;
