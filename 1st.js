// Showing the menu button
let menu = document.querySelector('#menu-btn');
// Getting the navbar element inside of the header
let navbar = document.querySelector('.header .flex .navbar');
menu.onclick = () =>{
   // The code below toggles the icon to switch between the icon and close icon
   menu.classList.toggle('fa-times');
   // This code below toggles the navbar visibility
   navbar.classList.toggle('active');
}
// When the use scrolls the page
window.onscroll = () =>{
   // Making sure the menu icon goes back to normal
   menu.classList.remove('fa-times');
   // Making sure to hide the navbar if it was opened
   navbar.classList.remove('active');
}
