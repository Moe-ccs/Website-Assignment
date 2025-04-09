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
