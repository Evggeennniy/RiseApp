// ANIMANIONS
const animatedSlideItem = document.querySelectorAll(".animated-slide");
function checkFade() {
  animatedSlideItem.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    if (rect.top <= windowHeight * 0.8) {
      item.classList.add("active");
    }
  });
}
window.addEventListener("scroll", checkFade);
window.addEventListener("load", checkFade);

// NAVIGATION
const navLinkToContact = document.querySelector(".nav__link-contactus");
const contactUsButton = document.querySelector(".why-us__contactus");
navLinkToContact.addEventListener("click", () => {
  contactUsButton.scrollIntoView({ behavior: "smooth", block: "start" });
});

// INTRODUCTION LEFTSIDE
const introDynamicTitle = document.querySelector(".intro__dynamic-title");
let introTitleChoices = document.querySelector(
  ".intro__title-choices"
).textContent;
introTitleChoices = introTitleChoices.split(","); // Исправлено создание массива

const delayBetweenTitles = 2000;
const letterChangeDelay = 50;

function changeTitle(index = 0) {
  const currentTitle = introTitleChoices[index];
  animateTitleChange(currentTitle, () => {
    setTimeout(() => {
      // Циклически переходит к следующему индексу
      changeTitle((index + 1) % introTitleChoices.length);
    }, delayBetweenTitles);
  });
}

function animateTitleChange(title, callback) {
  introDynamicTitle.textContent = "";
  let charIndex = 0;

  function addNextChar() {
    if (charIndex < title.length) {
      introDynamicTitle.textContent += title[charIndex];
      charIndex++;
      setTimeout(addNextChar, letterChangeDelay);
    } else {
      callback();
    }
  }

  addNextChar();
}

changeTitle();

// INTRODUCTION RIGHTSIDE
const discountBlock = document.querySelector(".discounts__content");
const discountDays = document.querySelector(".discounts__time-days");
const discountHours = document.querySelector(".discounts__time-hours");
const discountMinutes = document.querySelector(".discounts__time-minutes");
const discountSeconds = document.querySelector(".discounts__time-seconds");
const discountPercent = document.querySelector(".discounts__progressbar-title");
const discountProgresBar = document.querySelector(
  ".discounts__progressbar-done"
);
function updateTextContent(element, value) {
  if (element.textContent != value) {
    element.textContent = value;
  }
}

function changeTime() {
  const dateNow = new Date();
  const discountStart = new Date(2024, 5, 20);
  const discountsEnd = new Date(2024, 6, 6);
  const diff = discountsEnd - dateNow;
  const percents = Math.floor(diff / ((discountsEnd - discountStart) / 100));

  updateTextContent(discountDays, Math.floor(diff / (1000 * 60 * 60 * 24)));
  updateTextContent(discountHours, Math.floor((diff / (1000 * 60 * 60)) % 24));
  updateTextContent(discountMinutes, Math.floor((diff / (1000 * 60)) % 60));
  updateTextContent(discountSeconds, Math.floor((diff / 1000) % 60));
  updateTextContent(discountPercent, percents);

  discountProgresBar.style.width = `${percents}%`;

  setTimeout(changeTime, 1000);
}
setTimeout(changeTime, 300);

// POPUP
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
