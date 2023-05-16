document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#login");

    form.addEventListener("submit", event => {
        event.preventDefault();
        const username = document.querySelector("#username");
        const password = document.querySelector("#password");
        fetch(`/validate-user?username=${username.value}&password=${password.value}`)
            .then(response => response.json())
            .then(data => (
                alertPassWrong(data)
            ))
    })

    function alertPassWrong(data) {
        if (data.userExists === "true") {
            window.location.replace("/viewblogs");
        } else {
            alert("Wrong username or password");
            document.querySelectorAll(".loginInput").forEach(input => {
                input.value = "";
            })
        }
    }
})