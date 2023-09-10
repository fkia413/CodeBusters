const swiper = new Swiper('.swiper', {
	spaceBetween: 0,
	centeredSlides: true,
	autoplay: {
		delay: 2500,
		disableOnInteraction: false,
	},
	pagination: {
		el: '.swiper-pagination',
		type: 'bullets', // other options are "fraction" or "progressbar"
		clickable: true,
	},
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},

	on: {
		slideChange: function () {
			// get the current slide index (it's zero based)
			var currentSlide = swiper.realIndex;

			// remove the 'swiper-pagination-bullet-active' class from all indicators
			var indicators = document.querySelectorAll(
				'.swiper-pagination-bullet'
			);
			indicators.forEach(function (indicator) {
				indicator.classList.remove('swiper-pagination-bullet-active');
			});

			// add the 'swiper-pagination-bullet-active' class to the current indicator
			indicators[currentSlide].classList.add(
				'swiper-pagination-bullet-active'
			);
		},
	},
});
