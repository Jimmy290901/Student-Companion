var active_tab = "overview";
const modal_container = document.getElementById("modal_container");
const body = document.querySelector("body");

function show(tab) {
    const curr_tab = document.getElementById(active_tab.concat("_tab"));
    const select_tab = document.getElementById(tab.concat('_tab'));

    const curr_block = document.getElementById(active_tab.concat("_block"));
    const select_block = document.getElementById(tab.concat("_block"));
    
    curr_block.classList.add("no-display");
    select_block.classList.remove("no-display");
    
    curr_tab.classList.remove("tab-hghl");
    select_tab.classList.add("tab-hghl");
    
    active_tab = tab;
}

function show_modal() {
    modal_container.classList.add("modal_show");
    body.style.overflow = "hidden";
}

function hide_modal() {
    modal_container.classList.remove("modal_show");
    body.style.overflow = "auto";
}