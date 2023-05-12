const form = document.forms.myform;
var messageElem = document.getElementById("form-message");
let protectedBtn = document.getElementById("protected");
var protectedMessage = document.getElementById("message")

form.addEventListener("submit", (e) => {
    e.preventDefault()
    const formData = new FormData(form)
    const username = formData.get('username')
    const password = formData.get('password')

    fetch('http://localhost:5000/login',{
        method : "POST",
        credentials: "include",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        }),
    }).then(
        response => {
            return response.json()
        }
    ).then(
        response => {
            messageElem.innerHTML = "Akses Token Anda : " + response.access_token
            token = response.access_token
            user = username
            pass = password
        }
    )
})

protectedBtn.addEventListener("click", (e) =>{
    e.preventDefault()

    fetch('http://localhost:5000/protected', {
        method: "GET",
        credentials: "include",
        headers: {
            'Authorization': 'Bearer ' + token
        }
    }).then(
        response => {
            return response.json()
        }
    ).then(
        response => {
            console.log(response)
            let res = response.logged_in_as
            protectedMessage.innerHTML = "username: " + user + " password: " + pass
        }
    )
})