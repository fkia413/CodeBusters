// Get references to the movie and screening time select fields
const movieSelect = document.getElementById('{{ form.movie_id.id }}');
const screeningTimeSelect = document.getElementById(
	'{{ form.screening_time.id }}'
);

// Define an event listener to update the screening time choices when the movie is selected
movieSelect.addEventListener('change', () => {
	const selectedMovieId = movieSelect.value;
	// Make an AJAX request to fetch the screening times for the selected movie
	fetch(`/get_screening_times?movie_id=${selectedMovieId}`)
		.then((response) => response.json())
		.then((data) => {
			// Clear the current options
			screeningTimeSelect.innerHTML = '';
			// Populate the screening time options based on the retrieved data
			data.forEach((option) => {
				const newOption = document.createElement('option');
				newOption.value = option[0];
				newOption.textContent = option[1];
				screeningTimeSelect.appendChild(newOption);
			});
		});
});
