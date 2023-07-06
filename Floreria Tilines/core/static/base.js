document.addEventListener("DOMContentLoaded", () => {
    const suscribirBtn = document.getElementById("subscribir-btn");
    const emailInput = document.getElementById("email-input");
    const emailError = document.getElementById("email-error");

    function validarEmail(email) {
        return email.endsWith("@gmail.com") || email.endsWith("@hotmail.com");
    }

    suscribirBtn.addEventListener("click", () => {
        const email = emailInput.value;
        if (validarEmail(email)) {
            emailError.classList.add("hidden");
            alert("Suscrito!");
            emailInput.value = "";
            location.reload();
        } else {
            emailError.classList.remove("hidden");
            emailError.innerText = "Por favor, introduce un correo electrónico válido.";
        }
    });
});