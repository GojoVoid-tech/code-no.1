const button = document.querySelector("button");
const input = document.querySelector("input");
const result = document.getElementById("result");

button.addEventListener("click", function() {
    const city = input.value;
    result.innerText = "You searched for: " + city;
});