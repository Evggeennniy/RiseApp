function getCookie(name) {
  let cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    let [cookieName, cookieValue] = cookie.split("=");
    if (cookieName === name) {
      return cookieValue;
    }
  }
  return null;
}

function setCookie(name, value, days = 365, path = "/") {
  let expires = "";
  if (days) {
    let date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // переводим дни в миллисекунды
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = `${name}=${value}${expires}; path=${path}`;

  return value;
}

function generateUUID() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

const uuidField = document.getElementById("uuid-field");
function identifier() {
  let id = getCookie("id");

  if (!id) id = setCookie("id", generateUUID());

  uuidField.value = id;
}

identifier();

// ANIMANIONS
const animatedSlideItem = document.querySelectorAll(".animated-slide");
function checkFade() {
  animatedSlideItem.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    if (rect.top <= windowHeight * 0.85) {
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

// FORM
const formTrigger = document.getElementById("form-finder");
const form = document.querySelector(".contacts__form");
const formConfirm = document.querySelector(".contacts__button");
const phoneInput = document.getElementById("phone");

if (contactBtn) {
  contactBtn.addEventListener("click", () => {
    form.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}

form.addEventListener("submit", (e) => {
  if (phoneInput.value.length < 8) {
    e.preventDefault();
    alert("Сheck the phone number please");
    phoneInput.focus();
    return;
  }

  alert("Successfully delivered!! Thank you.");
});

phoneInput.addEventListener("input", () => {
  phoneInput.value = phoneInput.value.replace(/(?!^)\+|[^\d+]/g, "");
});

formTrigger.addEventListener("click", () => {
  form.scrollIntoView({ behavior: "smooth", block: "center" });
});
