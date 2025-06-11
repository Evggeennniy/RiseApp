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
  langButton.classList.toggle("active");
});

// INTRODUCTION
const contactBtns = document.querySelectorAll(".contacts-btn");
const contactBlock = document.querySelector(".aboutus__contacts");

// FORM
const form = document.querySelector(".contacts__form");
const formConfirm = document.querySelector(".contacts__button");
const phoneInput = document.getElementById("phone");

if (contactBtns) {
  for (let btn of contactBtns) {
    btn.addEventListener("click", () => {
      form.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  }
}

form.addEventListener("submit", (e) => {
  alert(`
    Successfully delivered!! Thank you.
    We'll answer as soon as possibly.
    RiseApp Company
  `);
});

phoneInput.addEventListener("input", () => {
  phoneInput.value = phoneInput.value.replace(/(?!^)\+|[^\d+]/g, "");
});

const serviceMenu = document.querySelector(".service__info-menu");
const serviceBtns = document.querySelectorAll(".service__info__menu__item");
const serviceContents = document.querySelectorAll(".service__info_main");
if (serviceMenu) {
  serviceMenu.addEventListener("click", (event) => {
    const target = event.target;
    if (target.classList.contains("service__info__menu__item")) {
      const targetContent = target.getAttribute("content");
      for (let btn of serviceBtns) {
        target === btn
          ? btn.classList.add("active")
          : btn.classList.remove("active");
      }
      for (let contentBlock of serviceContents) {
        contentBlock.getAttribute("content") == targetContent
          ? contentBlock.classList.add("active")
          : contentBlock.classList.remove("active");
      }
    }
  });
}

const getUpBtn = document.getElementById("get-up-btn");
if (getUpBtn) {
  getUpBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}
