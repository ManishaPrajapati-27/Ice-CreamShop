AOS.init({
  duration: 1500,
});

// Blog Carousel
$(".blog-carousel").owlCarousel({
  loop: true,
  margin: 0,
  //   nav: true,
  dots: false,
  autoplay: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 3,
    },
    1000: {
      items: 4,
    },
  },
});

// Card Carousel
$(".card-carousel").owlCarousel({
  loop: true,
  margin: 0,
  //   nav: true,
  autoplay: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 1,
    },
    1000: {
      items: 1,
    },
  },
});
