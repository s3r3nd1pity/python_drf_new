import {authService} from "./authService";
import {w3cwebsocket} from 'websocket'

const baseURL = 'ws://localhost/api'

const socketService = async () => {
    const {data} = await authService.getSocketToken();
    return {
        chat: (room) => new w3cwebsocket(`${baseURL}/chat/${room}/?token=${data}`),
        pizzas:()=>new w3cwebsocket(`${baseURL}/pizza/?token=${data}`)
    }
}

export {
    socketService
}