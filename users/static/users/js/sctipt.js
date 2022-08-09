//  burger start
let burger = document.querySelector('.header__burger');
let nav = document.querySelector('.header__menu');
let body = document.querySelector('body');
let link = document.querySelectorAll('.header__link');
let logo = document.querySelector('.header__logo');

burger.addEventListener('click', () => {
    nav.classList.toggle('active');
    burger.classList.toggle('active');
    body.classList.toggle('lock');
    if (body.classList.contains('lock')) {
        link[1].innerHTML = 'Войти в аккаунт';
    } else {
        setTimeout(() => {
            link[1].innerHTML = 'Войти';
        }, 500);
    }
})



document.addEventListener('keydown', (e) => {
    if (e.keyCode == 27) {
        nav.classList.remove('active');
        burger.classList.remove('active');
        body.classList.remove('lock');
    }
})
// burger end