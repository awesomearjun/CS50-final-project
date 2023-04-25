const showPasswordButton = document.querySelector("#showPass");
const passwordInput = document.querySelector("#password");

if (showPasswordButton.checked) {
    passwordInput.type = "text";
} else {
    passwordInput.type = "password";
}