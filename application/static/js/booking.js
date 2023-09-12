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

    // Event listener for movie selection
    movieSelect.on('change', () => {
        const selectedMovieId = movieSelect.val();

        // Make an AJAX request to fetch the screening times for the selected movie
        $.ajax({
            url: `/get_screening_times?movie_id=${selectedMovieId}`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Clear the current options
                screeningTimeSelect.empty();

                // Populate the screening time options based on the retrieved data
                $.each(data, function (index, option) {
                    screeningTimeSelect.append(
                        $('<option>', {
                            value: option[0],
                            text: option[1],
                        })
                    );
                });
            },
            error: function (error) {
                console.error('Error fetching screening times:', error);
            },
        });
    });

    // Event listener for adult and child ticket inputs
    adultTicketsInput.on('input', updateTotalPrice);
    childTicketsInput.on('input', updateTotalPrice);
});



