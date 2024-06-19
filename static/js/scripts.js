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

const popupButtonOutside = document.querySelector(".popup__button-outside");
const popupButtonInside = document.querySelector(".popup__button-inside");
const popupOverlay = document.querySelector(".popup__overlay");
const popupMessage = document.querySelector(".popup__message");
function togglePopup(event) {
  if (event.target.classList.contains("popup__toggle")) {
    popupOverlay.classList.toggle("active");
    popupMessage.classList.toggle("active");
    document.body.classList.toggle("no-scroll");
  }
}
popupButtonOutside.addEventListener("click", togglePopup);
popupButtonInside.addEventListener("click", togglePopup);
