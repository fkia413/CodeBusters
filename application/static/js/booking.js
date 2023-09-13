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

			// populating screening times select field
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
	// checking if the movie_id is already selected (i.e., user accessed booking page from movie details pages)
	const movie_id = movieDropdown.value;

	if (movie_id != '-1') {
		displayScreenTypes(movie_id);
	}

	// adding initial select option to screening time dropdown
	const newOption = document.createElement('option');
	const optionText = document.createTextNode('Select');
	newOption.appendChild(optionText);
	newOption.setAttribute('value', '-1');
	newOption.selected = true;
	newOption.disabled = true;
	screeningTimeDropdown.appendChild(newOption);

	// adding initial select option to screen type time dropdown
	const newOption2 = document.createElement('option');
	const optionText2 = document.createTextNode('Select');
	newOption2.appendChild(optionText2);
	newOption2.setAttribute('value', '-1');
	newOption.selected = true;
	newOption.disabled = true;
	screenTypesDropdown.appendChild(newOption2);

	// resetting selected movie

	// initial update of prices
	updateTotalPrice();

	childTicketInput.addEventListener('input', updateTotalPrice);
	adultTicketInput.addEventListener('input', updateTotalPrice);

	// event listeners for movie selection
	movieDropdown.addEventListener('change', () => {
		// get movie_id
		const movie_id = movieDropdown.value;

		if (movie_id === '-1') {
			// clear existing options
			// this is just for extra security, should not be needed

			screeningTimeDropdown.innerHTML = '';
			const newOption = document.createElement('option');
			const optionText = document.createTextNode('Select');
			newOption.appendChild(optionText);
			newOption.setAttribute('value', '-1');
			screeningTimeDropdown.appendChild(newOption);
		} else {
			displayScreenTypes(movie_id);

			const selectedScreenType = screenTypesDropdown.value;
			const selectedMovieId = movieDropdown.value;
			displayScreeningTimes(selectedMovieId, selectedScreenType);
		}
	});

	// event listener for screen type selection
	screenTypesDropdown.addEventListener('change', () => {
		const selectedScreenType = screenTypesDropdown.value;
		const selectedMovieId = movieDropdown.value;

		displayScreeningTimes(selectedMovieId, selectedScreenType);
	});
});
