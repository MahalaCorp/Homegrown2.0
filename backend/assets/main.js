// // loader elements
// const loader = document.getElementById("loader");
// const main = document.getElementById("main");

// function download() {
//     if (document.all) {
//         loader.classList.add("hidden");
//         loader.classList.remove("flex");

//         main.classList.add("flex");
//         main.classList.remove("hidden");
//     } else if (document.getElementById) {
//         node = document.getElementById("loader").classList = "hidden";
//         node = document.getElementById("main").classList = "flex";
//     }
// }

//navigation elements
const bars = document.getElementById("bars");
const nav = document.getElementById("nav");
const main = document.getElementsByTagName('main');

bars.addEventListener('click', () => {
    if (nav.classList.contains("hidden")) {
        nav.classList.remove('hidden');
        nav.classList.add('flex');
    } else {
        nav.classList.remove('flex');
        nav.classList.add('hidden')
    }
})

main.addEventListener('click', () => {
    if (nav.classList.contains('flex')) {
        nav.classList.remove('flex');
        nav.classList.add('hidden')
    }
})