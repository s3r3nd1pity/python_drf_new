import {useEffect, useState} from "react";
import {pizzaService} from "../services/pizzaService";
import PIzzaComponent from "./PIzzaComponent";
import {socketService} from "../services/socketService";

const PizzasComponent = () => {
    const [pizzas, setPizzas] = useState([])
    const [trigger, setTrigger] = useState(null)
    useEffect(() => {
        pizzaService.getAll().then(({data}) => setPizzas(data.data))

    }, [trigger]);

    useEffect(() => {
        socketInit().then()
    }, []);

    const socketInit = async () => {
        const {pizzas} = await socketService()
        const client = await pizzas()

        client.onopen = () => {
            console.log("Pizza socket connected")
            const payload = {
                action: "subscribe_to_pizza_model_changes",
                request_id: new Date().getTime()
            }
            client.send(JSON.stringify(payload))
        }


        client.onmessage = ({data}) => {
            console.log(data);
            setTrigger(prev => !prev)
        }

    }
    return (
        <div>
            {
                pizzas.map(value => <PIzzaComponent pizza={value} key={value.id}/>)
            }
        </div>
    );
};

export default PizzasComponent;