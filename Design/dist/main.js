// loader elements
const loader = document.getElementById("loader");
const main = document.getElementById("main");

function download() {
    if (document.all) {
        loader.classList.add("hidden");
        loader.classList.remove("flex");

        main.classList.add("flex");
        main.classList.remove("hidden");
    } else if (document.getElementById) {
        node = document.getElementById("loader").classList = "hidden";
        node = document.getElementById("main").classList = "flex";
    }
}

//navigation elements
const bars = document.getElementById("bars");
const nav = document.getElementById("nav");

bars.addEventListener('click', () => {
    if (nav.classList.contains("hidden")) {
        nav.classList.remove('hidden');
        nav.classList.add('flex');
    } else {
        nav.classList.remove('flex');
        nav.classList.add('hidden')
    }
})

// // talent visiblity
// const talent = document.getElementById("talent");
// const info = document.getElementById("info");

// talent.addEventListener('mouseover', () => {
//     if (info.classList.contains("hidden")) {
//         info.classList.remove('hidden');
//         info.classList.add('flex');
//     }
// })
// talent.addEventListener('mouseout', () => {
//     if (info.classList.contains("flex")) {
//         info.classList.remove('flex');
//         info.classList.add('hidden');
//     }
// })