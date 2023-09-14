'use strict';

// selectors
const movieDropdown = document.querySelector('.movie-list');
const screeningTimeDropdown = document.querySelector('.screening-times');
const screenTypesDropdown = document.querySelector('.screen-types');
const childTicketInput = document.querySelector('.child-ticket-input');
const adultTicketInput = document.querySelector('.adult-ticket-input');
const totalPriceField = document.querySelector('.total-price');

// functionality
function displayScreeningTimes(movie_id, screen_type) {
	axios
		.get(`/get_screening_times/${movie_id}/${screen_type}`)
		.then((response) => {
			// clear existing options
			screeningTimeDropdown.innerHTML = '';

			const disabledSelectOption = document.createElement('option');
			const disabledSelectOptionText = document.createTextNode('Select');
			disabledSelectOption.appendChild(disabledSelectOptionText);
			disabledSelectOption.disabled = true;
			disabledSelectOption.setAttribute('value', '-1');
			screeningTimeDropdown.appendChild(disabledSelectOption);

			const options = response.data;

			// populating screening times select field
			for (let option of options) {
				const newOption = document.createElement('option');
				const optionText = document.createTextNode(option);
				newOption.appendChild(optionText);
				newOption.setAttribute('value', option);
				screeningTimeDropdown.appendChild(newOption);
			}
		})
		.catch((error) => {
			console.error('Error retrieving movie id:', error);
		});
}

function displayScreenTypes(movie_id) {
	axios
		.get(`/get_screen_types/${movie_id}`)
		.then((response) => {
			// clear existing options
			screenTypesDropdown.innerHTML = '';

			const disabledSelectOption = document.createElement('option');
			const disabledSelectOptionText = document.createTextNode('Select');
			disabledSelectOption.appendChild(disabledSelectOptionText);
			disabledSelectOption.disabled = true;
			disabledSelectOption.setAttribute('value', '-1');
			screenTypesDropdown.appendChild(disabledSelectOption);

			const options = response.data;

			let isFirstOption = true;

			// populating screening types select field
			for (let option of options) {
				const newOption = document.createElement('option');
				const optionText = document.createTextNode(option);
				newOption.appendChild(optionText);
				newOption.setAttribute('value', option);

				if (isFirstOption) {
					newOption.selected = true;
					isFirstOption = false;
				}

				screenTypesDropdown.appendChild(newOption);
			}

			const selectedScreenType = screenTypesDropdown.value;
			const selectedMovieId = movieDropdown.value;

			displayScreeningTimes(selectedMovieId, selectedScreenType);
		})
		.catch((error) => {
			console.error('Error retrieving movie id:', error);
		});
}

// updating total price in booking form
function updateTotalPrice() {
	axios
		.get('get_ticket_prices')
		.then((response) => {
			const adultTicketPrice = parseFloat(response.data.adult_price);
			const childTicketPrice = parseFloat(response.data.child_price);

			// console.log(adultTicketPrice, childTicketPrice); // debug

			// calculate and display total price
			const adultTickets = parseInt(adultTicketInput.value) || 0;
			const childTickets = parseInt(childTicketInput.value) || 0;

			const total =
				adultTicketPrice * adultTickets +
				childTicketPrice * childTickets;
			totalPriceField.value = total.toFixed(2);
		})
		.catch((error) => {
			console.error('Error fetching ticket prices', error);
		});
}

// event listeners
document.addEventListener('DOMContentLoaded', () => {
	// adding initial select option to screening time dropdown
	const newOption = document.createElement('option');
	const optionText = document.createTextNode('Select');
	newOption.appendChild(optionText);
	newOption.setAttribute('value', '-1');
	newOption.selected = true;
	newOption.disabled = true;
	screeningTimeDropdown.appendChild(newOption);

	// adding initial select option to screen type dropdown
	const newOption2 = document.createElement('option');
	const optionText2 = document.createTextNode('Select');
	newOption2.appendChild(optionText2);
	newOption2.setAttribute('value', '-1');
	newOption2.selected = true;
	newOption2.disabled = true;
	screenTypesDropdown.appendChild(newOption2);

	// checking if the movie_id is already selected (i.e., user accessed booking page from movie details pages)
	const movie_id = movieDropdown.value;

	// if user accesses booking page through movie details page, there is already a selected movie_id
	// we populate screen type and screening time dropdowns immediately with the first option selected
	if (movie_id != '-1') {
		displayScreenTypes(movie_id);
	}

	// on change listener for the movie dropdown
	movieDropdown.addEventListener('change', () => {
		// get movie_id
		const movie_id = movieDropdown.value;
		// display screen types based on movie selection
		displayScreenTypes(movie_id);
		// display screening times based on movie and screen type selection
		const selectedScreenType = screenTypesDropdown.value;
		displayScreeningTimes(movie_id, selectedScreenType);
	});

	// on change listener for the screen type dropdown
	screenTypesDropdown.addEventListener('change', () => {
		const selectedScreenType = screenTypesDropdown.value;
		const selectedMovieId = movieDropdown.value;
		displayScreeningTimes(selectedMovieId, selectedScreenType);
	});

	// initial update of prices
	updateTotalPrice();

	// updating price on ticket amount change
	childTicketInput.addEventListener('input', updateTotalPrice);
	adultTicketInput.addEventListener('input', updateTotalPrice);
});
