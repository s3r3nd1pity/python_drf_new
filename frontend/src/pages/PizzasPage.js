import PizzaForm from "../components/PizzaForm";
import PizzasComponent from "../components/PizzasComponent";
import ChatComponent from "../components/ChatComponent";

const PizzasPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <hr/>
            <ChatComponent/>
        </div>
    );
};

export default PizzasPage;