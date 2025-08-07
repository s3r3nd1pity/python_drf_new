export const baseURL = "/api"

const authPath = "/auth"

const pizzasPath= "/pizza"

export const urls = {
    auth:{
        login:authPath,
        socket:`${authPath}/socket`
    },
    pizzas:pizzasPath
}