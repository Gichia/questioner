const menuIcon = document.getElementById('menu-icon');
const slideOutMenu = document.getElementById('slideout-menu');
const searchIcon = document.getElementById('search-icon');
const searchBox = document.getElementById('searchbox');

searchIcon.addEventListener('click', () => {
    if(searchBox.style.top == '72px') {
        searchBox.style.top = '24px';
        searchBox.style.pointerEvents = 'none';
    } else {
        searchBox.style.top = '72px';
        searchBox.style.pointerEvents = 'auto';
    }
});

menuIcon.addEventListener('click', () => {
    if(slideOutMenu.style.opacity == '1') {
        slideOutMenu.style.opacity = '0';
        slideOutMenu.style.pointerEvents = 'none';
    } else {
        slideOutMenu.style.opacity = '1';
        slideOutMenu.style.pointerEvents = 'auto';
    }
});