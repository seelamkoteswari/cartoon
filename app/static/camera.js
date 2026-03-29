const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => video.srcObject = stream);

document.addEventListener("keydown", function(e) {
    if (e.code === "Space") {
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;

        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0);

        const image = canvas.toDataURL("image/png");

        fetch("/capture", {
            method: "POST",
            body: JSON.stringify({ image: image }),
            headers: { "Content-Type": "application/json" }
        });

        alert("Captured!");
    }
});