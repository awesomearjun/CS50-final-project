function showHidePass() {
    const passInput = document.querySelector("#password");

    if (passInput.type === "password") {
        passInput.type = "text";
    } else {
        passInput.type = "password";
    }
}