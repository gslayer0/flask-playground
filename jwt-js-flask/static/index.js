
console.log("start the game")

const btnLogin = document.querySelector("#btn-login");
const inptNama = document.querySelector("#nama");
const inptPassword = document.querySelector("#password");
const loginInfo = document.querySelector("#login-info")
const userInfo = document.querySelector("#user-info")
const bntCheck = document.querySelector("#btn-check")

btnLogin.addEventListener("click", async () => {
    loginInfo.innerHTML = ""
    let name = inptNama.value
    let password = inptPassword.value
    let loginUrl = "http://127.0.0.1:5000/login"

    let resp = await fetch(loginUrl, {
        method: "POST",
        body: JSON.stringify({
            name: name,
            password: password
        }),
        headers: {
            "Content-type": "application/json"
        }
    });
    let data = await resp.json();
    console.log(data)
    loginInfo.innerHTML = data["message"];
})

bntCheck.addEventListener("click", async () => {
    let checkUrl = "http://127.0.0.1:5000/check"
    let resp = await fetch(checkUrl, {
        method: "GET",
    })
    let data = await resp.json();
    console.log(data)
    if( "data" in data ) {
        userInfo.innerHTML = JSON.stringify(data["data"])
    } else {
        userInfo.innerHTML = data["message"]
    }
})