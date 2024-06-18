const animatedSlideItem = document.querySelectorAll(".animated-slide");
function checkFade() {
  animatedSlideItem.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    if (rect.top <= windowHeight * 0.7) {
      item.classList.add("active");
    }
  });
}
window.addEventListener("scroll", checkFade);
window.addEventListener("load", checkFade);

const navLinkToPortfolio = document.querySelector(".nav__link-portfolio");
const portfolioIntro = document.querySelector(".portfolio__intro");
navLinkToPortfolio.addEventListener("click", () => {
  portfolioIntro.scrollIntoView({ behavior: "smooth", block: "start" });
});

const popup = document.querySelector(".popup");
const popupOverlay = document.querySelector(".popup__overlay");
const popupMessage = document.querySelector(".popup__message");
popup.addEventListener("click", (event) => {
  if (event.target.classList.contains("popup__toggle")) {
    popupOverlay.classList.toggle("active");
    popupMessage.classList.toggle("active");
  }
});
