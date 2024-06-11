console.log("Haloo!")

const input = document.querySelector("#input")
const printer = document.querySelector("#printer")

printer.innerHTML = localStorage.getItem("value")

input.addEventListener("keyup", () => {
    localStorage.setItem('value', input.value)
    printer.innerHTML = localStorage.getItem("value")
});