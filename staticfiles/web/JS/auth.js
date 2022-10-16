
const register = (redirectURL) => {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value; 
    const errorText = document.getElementById("error-text")
    
    if(password !== confirmPassword){
        errorText.innerHTML = "Passwords don't match!"
        return;
    }

    axios.post('http://127.0.0.1:8000/register/', {username, email, password})
        .then(res => {
            console.log(res)
            return res
        })
        .then(data => {
            setCookie("token", data.token, 1)
            setCookie("username", username, 1)
            setCookie("email", email, 1)
            window.location = redirectURL
        })
        .catch(err => {
            errorText.innerHTML = err.message
        })
}

const login = () => {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const errorText = document.getElementById("error-text")

    axios.post('http://127.0.0.1:8000/login/', {username, email, password})
        .then(res => {
            return res.data
        })
        .then(data => {
            setCookie("token", data.token, 1)
            setCookie("username", username, 1)
            setCookie("email", email, 1)
            window.location = redirectURL
        })
        .catch(err => {
            errorText.innerHTML = err.message
            console.error(err.message)
        })
}

const requestResetPassword = () => {
    const email = document.getElementById("email").value;
    const errorText = document.getElementById("error-text")

    axios.post('http://127.0.0.1:8000/reset_password/', {email})
        .then(res => {
            return res.data
        })
        .catch(err => {
            errorText.innerHTML = err.message
            console.error(err.message)
        })
}

const resetPassword = () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value; 
    const errorText = document.getElementById("error-text")
    
    if(password !== confirmPassword){
        errorText.innerHTML = "Passwords don't match!"
        return;
    }

    axios.put('http://127.0.0.1:8000/reset_password/', {email, password})
        .then(res => {
            return res.data
        })
        .catch(err => {
            errorText.innerHTML = err.message
            console.error(err.message)
        })
}