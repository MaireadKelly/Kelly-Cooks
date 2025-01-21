// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Select all rating stars
    const stars = document.querySelectorAll(".star");
    const ratingInput = document.getElementById("id_rating");

    if (stars && ratingInput) {
        // Function to handle star hover
        const highlightStars = (index) => {
            stars.forEach((star, idx) => {
                star.classList.toggle("highlighted", idx <= index);
            });
        };

        // Function to handle star selection
        const selectRating = (index) => {
            ratingInput.value = index + 1; // Set rating value
            stars.forEach((star, idx) => {
                star.classList.toggle("selected", idx <= index);
            });
        };

        // Add event listeners for each star
        stars.forEach((star, index) => {
            star.addEventListener("mouseover", () => highlightStars(index));
            star.addEventListener("mouseout", () => highlightStars(ratingInput.value - 1));
            star.addEventListener("click", () => selectRating(index));
        });

        // Highlight the pre-selected rating (if any)
        if (ratingInput.value) {
            const preSelectedIndex = parseInt(ratingInput.value, 10) - 1;
            highlightStars(preSelectedIndex);
            selectRating(preSelectedIndex);
        }
    }
});
