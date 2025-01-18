let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.imagemdiv');
    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }

    const offset = -currentIndex * 100;
    document.querySelector('.imagens').style.transform = `translateX(${offset}%)`;
}
function showSlideG(index) {
    const slides = document.querySelectorAll('.imagemdivG');
    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }

    const offset = -currentIndex * 100;
    document.querySelector('.imagensG').style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}
function nextSlideG() {
    showSlideG(currentIndex + 1);
}

function prevSlideG() {
    showSlideG(currentIndex - 1);
}