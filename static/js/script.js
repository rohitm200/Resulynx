const revealCards = () => {
    document.querySelectorAll(".card").forEach((card) => {
        const position = card.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }
    });
};

window.addEventListener("scroll", revealCards);
window.addEventListener("load", revealCards);

const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");

const showFileName = () => {
    if (!fileInput || !fileName) return;
    fileName.textContent = fileInput.files.length ? fileInput.files[0].name : "No file selected";
};

if (dropArea && fileInput) {
    dropArea.addEventListener("click", (event) => {
        if (event.target.closest("button") || event.target.closest("input")) return;
        fileInput.click();
    });

    dropArea.addEventListener("dragover", (event) => {
        event.preventDefault();
        dropArea.classList.add("is-dragging");
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.classList.remove("is-dragging");
    });

    dropArea.addEventListener("drop", (event) => {
        event.preventDefault();
        dropArea.classList.remove("is-dragging");
        fileInput.files = event.dataTransfer.files;
        showFileName();
    });

    fileInput.addEventListener("change", showFileName);
}
