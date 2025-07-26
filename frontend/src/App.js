import {useEffect, useState} from "react";
import axios from "axios";

function App() {
    const [pizzas, setPizzas] = useState([])
    useEffect(() => {
        axios.get('/api/pizza').then(({data})=>setPizzas(data.data))
    }, []);
  return (
    <div className="App">
        {pizzas.map(value => <div> {value.name}</div>)}
        </div>
  );
}

export default App;
