window.addEventListener("scroll", () => {
    document.querySelectorAll(".card").forEach(card => {
        let position = card.getBoundingClientRect().top;
        let screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }
    });
});

const dropArea = document.getElementById("drop-area");

if (dropArea) {
    dropArea.addEventListener("click", () => {
        document.getElementById("fileInput").click();
    });

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.style.border = "2px dashed #38bdf8";
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.style.border = "2px dashed rgba(255,255,255,0.08)";
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        document.getElementById("fileInput").files = e.dataTransfer.files;
    });
}
