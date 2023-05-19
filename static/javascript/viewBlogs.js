document.addEventListener("DOMContentLoaded", () => {
    const blogButton = document.querySelector(".blog");
    const blogModal = document.querySelector("dialog");
    
    blogButton.addEventListener("click", () => {
        blogModal.showModal();
    });
})