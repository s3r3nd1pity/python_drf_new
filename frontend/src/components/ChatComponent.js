import {useEffect, useRef, useState} from "react";
import {socketService} from "../services/socketService";

const ChatComponent = () => {
    const [room, setRoom] = useState(null)
    const [socketClient, setSocketClient] = useState(null)
    const [messages, setMessages] = useState([])
    const roomInput = useRef();

    useEffect(() => {
        if (room) {
            socketInit(room).then(value => setSocketClient(value))
        }
    }, [room]);

    const socketInit = async (room) => {
        const {chat} = await socketService()
        const client = await chat(room)

        client.onopen = () => {
            console.log("chat socket connect");
        }

        client.onmessage = ({data}) => {
            const {message, user} = JSON.parse(data.toString());
            setMessages(prevState => [...prevState, {user, message}])
        }

        return client
    }

    const roomHandler = () => {
        setRoom(roomInput.current.value)
    }

    const enterKey = (event) => {
        if (event.key === "Enter") {
            socketClient.send(JSON.stringify({
                data: event.target.value,
                action: "send_message",
                request_id: new Date().getTime(),
            }))
            event.target.value = ""
        }
    }
    return (
        <div>
            {
                !room ? <div>
                    <input type={"text"} ref={roomInput}/>
                    <button onClick={roomHandler}>Go to rom</button>
                </div> : <div>
                    {
                        messages.map(value => <div>{value.user}:{value.message}</div>)

                    }
                    <input type={"text"} onKeyDown={enterKey}/>
                </div>
            }
        </div>
    );
};

export default ChatComponent;