document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("submit", event => {
        event.preventDefault();
        const title = document.querySelector("#title").value;
        const description = document.querySelector("#description").value;
        const content = document.querySelector("#content").value;
        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;

        fetch(`/validate-user?username=${username}&password=${password}`)
            .then(response => response.json())
            .then(data => (
               createBlog(data)
            ))

        function createBlog(data) {
            console.log(data);
            if (!data.userExists === "true") alert("Username or password wrong")

            const xhttp = new XMLHttpRequest();
            const postObject = {
                username: username,
                password: password,
                title: title,
                description: description,
                content: content,
            }
            const post = JSON.stringify(postObject)
            console.log(post);
            xhttp.open("POST", "/createblog", false);
            xhttp.setRequestHeader("Content-Type", "application/json");
            xhttp.send(post);
            window.location.replace("/viewblogs")
        }
    });
});