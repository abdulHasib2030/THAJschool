$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
      loop: true,          // Enable loop
      margin: 10,          // Margin between items
      nav: true,           // Display navigation arrows
     
      responsive: {
          0: {
              items: 1    // Number of items to display at different screen sizes
          },
          600: {
              items: 2
          },
          1000: {
              items: 3
          }
      }
  });
});

// Header carousel
$(".header-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1500,
    items: 1,
    dots: false,
    loop: true,
    nav : true,
    navText : [
        '<i class="bi bi-chevron-left"></i>',
        '<i class="bi bi-chevron-right"></i>'
    ]
});
