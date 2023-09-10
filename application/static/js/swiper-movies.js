// Swiper
// create thumbs swiper
var thumbsSwiper = new Swiper('.thumbsSwiper', {
	spaceBetween: 10,
	slidesPerView: 5,
	breakpoints: {
		200: {
			slidesPerView: 1.5,
		},
		400: {
			slidesPerView: 1.5,
		},
		600: {
			slidesPerView: 3,
		},
		1100: {
			slidesPerView: 5,
		},
	},
	freeMode: true,
	watchSlidesProgress: true,
});

const swiper = new Swiper('.bannerSwiper', {
	spaceBetween: 0,
	effect: 'fade',

	// If we need pagination
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
	},

	// Navigation arrows
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},
	// Make thumbs slider works as thumbs for the banner slider
	thumbs: {
		swiper: thumbsSwiper,
	},
});
// Change titles
var changeTitle = (index) => {
	var title = document.querySelector('#title');
	var subTitle = document.querySelector('#sub-title');
	var desc = document.querySelector('#desc');
	title.innerHTML = `<h1>${titles[index].title}</h1>`;
	subTitle.innerHTML = `<p>${titles[index].subTitle}</p>`;
	desc.innerHTML = `<p>${titles[index].desc}</p>`;
};
// activeIndexChange is a swiper event
swiper.on('activeIndexChange', function () {
	changeTitle(swiper.activeIndex); // activeIndex is a swiper param
});
// Show overlay and change trailer video according to the active slider
var overlay = document.querySelector('.overlay');
var videoContainer = document.querySelector('#movie-trailer');
var showTrailer = () => {
	var index = swiper.activeIndex;
	videoContainer.innerHTML = `
  <video controls autoplay id ="video">
  <source src="assets/${titles[index].videoURL}" type="video/mp4">
  </video>
  `;
	overlay.classList.add('show');
};
// Close overlay
var closeOverlay = () => {
	// pause the video when close overlay
	var video = document.querySelector('#video');
	video.pause();
	overlay.classList.remove('show');
};
