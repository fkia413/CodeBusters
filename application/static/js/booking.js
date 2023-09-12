// Define an event listener to update the screening time choices when the movie is selected
$(document).ready(function () {
    const movieSelect = $('#{{ form.movie_id.id }}');
    const screeningTimeSelect = $('#{{ form.screening_time.id }}');
    const adultTicketsInput = $('#{{ form.adult_tickets.id }}');
    const childTicketsInput = $('#{{ form.child_tickets.id }}');
    const totalPriceInput = $('#{{ form.total_price.id }}');

    // Function to update the total price
    function updateTotalPrice() {
        // Fetch ticket prices from the server using an AJAX request
        $.ajax({
            url: '/get_ticket_prices',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Replace placeholders with actual ticket prices
                const adultTicketPrice = parseFloat(data.adult_price);
                const childTicketPrice = parseFloat(data.child_price);

                const adultTickets = parseInt(adultTicketsInput.val()) || 0;
                const childTickets = parseInt(childTicketsInput.val()) || 0;

                const total = adultTicketPrice * adultTickets + childTicketPrice * childTickets;
                totalPriceInput.val(total.toFixed(2)); // Update the total price input field
            },
            error: function (error) {
                console.error('Error fetching ticket prices:', error);
            },
        });
    }

    // Initial update of total price
    updateTotalPrice();

        // JavaScript to load screening times based on the selected movie
        const movieDropdown = document.getElementById("{{ form.movie_id.id }}");
        const screeningTimeDropdown = document.getElementById("{{ form.screening_time.id }}");
    
        movieDropdown.addEventListener("change", () => {
            const selectedMovieId = movieDropdown.value;
            fetch(`/get_screening_times?movie_id=${selectedMovieId}`)
                .then((response) => response.json())
                .then((data) => {
                    // Clear existing options
                    screeningTimeDropdown.innerHTML = "";
                    // Populate the screening time dropdown with new options
                    data.forEach((option) => {
                        const optionElement = document.createElement("option");
                        optionElement.value = option[0];
                        optionElement.textContent = option[1];
                        screeningTimeDropdown.appendChild(optionElement);
                    });
                });
        });

    // Event listener for adult and child ticket inputs
    adultTicketsInput.on('input', updateTotalPrice);
    childTicketsInput.on('input', updateTotalPrice);
});



