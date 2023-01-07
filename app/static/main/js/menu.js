let responsiveNavbar = document.querySelector("#responsive_navbar");
let sideBar = document.querySelector("#responsive_navbar div");
let close = document.querySelector("#close");

responsiveNavbar.addEventListener("click", function () {
  sideBar.classList.toggle("d-none");
});

close.addEventListener("click", function () {
  responsiveNavbar.classList.remove("active");
});

// Search

const tabTestimonials = Array.from(document.querySelectorAll(" .search-tab"));
const tabContents = Array.from(document.querySelectorAll(".search_result"));

const clearActives = function () {
  tabTestimonials.forEach((tabTestimonial) => {
    tabTestimonial.classList.remove("active");
  });
  tabContents.forEach((tabContent) => {
    tabContent.classList.remove("active");
  });
};

tabTestimonials.forEach((tabTestimonial) => {
  tabTestimonial.onclick = function () {
    clearActives();
    const targetId = tabTestimonial.getAttribute("data-target");
    const targetContent = document.getElementById(targetId);
    tabTestimonial.classList.add("active");
    targetContent.classList.add("active");
  };
});
