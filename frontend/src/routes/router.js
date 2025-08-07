import {createBrowserRouter, Navigate} from "react-router-dom";
import MainLayout from "../layouts/MainLayout";
import LoginPage from "../pages/LoginPage";
import PizzasPage from "../pages/PizzasPage";

export const router = createBrowserRouter([
    {
        path:"", element:<MainLayout/>, children:[
            {
                index:true, element:<Navigate to={"login"}/>
            },
            {
                path:"login", element:<LoginPage/>
            },
            {
                path:"pizzas", element:<PizzasPage/>
            }
        ]
    }
])