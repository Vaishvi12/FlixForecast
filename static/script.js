 <script>
        document.getElementById("showOverlayButton").addEventListener("click", function () {
            const whiteOverlay = document.getElementById("whiteOverlay");
            whiteOverlay.style.display = "block";

            // To ensure the overlay is visible, use a small delay (adjust as needed)
            setTimeout(function () {
                whiteOverlay.style.opacity = 1;
            }, 10);
        });
    </script> 