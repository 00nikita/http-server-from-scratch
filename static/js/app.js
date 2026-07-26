console.log("JavaScript loaded successfully!");

const button = document.getElementById("helloBtn");
const message = document.getElementById("message");

button.addEventListener("click", function () {
    message.textContent = "Hello from app.js! 🎉";
});