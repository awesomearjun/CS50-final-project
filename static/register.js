document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("submit", event => {
        event.preventDefault();
        const username = document.querySelector("#username").value;
        fetch(`/username-exists?username=${username}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.usernameExists) {
                    alert("Username already exists");
                }
            })
    });
});