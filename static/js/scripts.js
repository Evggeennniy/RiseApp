// ANIMANIONS
const animatedSlideItem = document.querySelectorAll(".animated-slide");
function checkFade() {
  animatedSlideItem.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    if (rect.top <= windowHeight * 0.75) {
      item.classList.add("active");
    }
  });
}
window.addEventListener("scroll", checkFade);
window.addEventListener("load", checkFade);

// NAVIGATION
const navButton = document.querySelector(".nav__link-portfolio");
const portfolioBlock = document.querySelector(".portfolio");
navButton.addEventListener("click", () => {
  portfolioBlock.scrollIntoView({ behavior: "smooth", block: "start" });
});
const langButton = document.querySelector(".lang-toggle");
const langMenu = document.querySelector(".nav__lang-menu-wrapper");
langButton.addEventListener("click", () => {
  langMenu.classList.toggle("visible");
});

// INTRODUCTION
const contactBtn = document.getElementById("intro-contacts-btn");
const contactBlock = document.querySelector(".aboutus__contacts");
contactBtn.addEventListener("click", () => {
  contactBlock.scrollIntoView({ behavior: "smooth", block: "start" });
});
