document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("submit", event => {
        event.preventDefault();
        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;
        fetch(`/username-exists?username=${username}`)
            .then(response => response.json())
            .then(data => {
                if (data.usernameExists) {
                    alert("Username already exists");
                } else {
                    const xhttp = new XMLHttpRequest();
                    const postObject = {
                        username: username,
                        password: password,
                    }
                    const post = JSON.stringify(postObject)
                    console.log(post);
                    xhttp.open("POST", "/register", true);
                    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                    xhttp.send(post);
                }
            })
    });
});