const animatedSlideItem = document.querySelectorAll(".animated-slide");
function checkFade() {
  animatedSlideItem.forEach((item) => {
    const rect = item.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    if (rect.top <= windowHeight * 0.6) {
      item.classList.add("active");
    }
  });
}

window.addEventListener("scroll", checkFade);
window.addEventListener("load", checkFade);
