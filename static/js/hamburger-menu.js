const navToggle = document.getElementById("nav-toggle");
const navMenu = document.getElementById("nav-menu");

navToggle.addEventListener("click", openMenu);

function openMenu() {
    navMenu.classList.toggle("active");
}