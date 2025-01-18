document.getElementById('toggleMenu').addEventListener('click', () => {
    const leftMenu = document.querySelector('.left-menu');
    leftMenu.style.display = leftMenu.style.display === 'none' ? 'block' : 'none';
});

function adjustPageSize() {
    const width = window.innerWidth;
    const scale = 
        width <= 600 ? 0.5 :
        width <= 700 ? 0.75 :
        width <= 767 ? 0.8 :
        width <= 1600 ? 0.9 : 1;

    document.body.style.transform = `scale(${scale})`;
}

window.addEventListener('resize', adjustPageSize);
adjustPageSize();
