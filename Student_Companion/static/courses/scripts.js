// const fdp_button = document.getElementById("fdp_button");
// const ger_button = document.getElementById("ger_button");
// const major_button = document.getElementById("major_button");
// const elective_button = document.getElementById("elective_button");

// const fdp_block = document.getElementById("fdp");
// const ger_block = document.getElementById("ger");
// const major_block = document.getElementById("major");
// const elective_block = document.getElementById("elective");

var active_blockname = "fdp";
var active_btn_name = "fdp_button";

function highlight_btn(btn_name) {
    const active_btn = document.getElementById(active_btn_name);
    active_btn.classList.remove("btn-secondary");
    active_btn.classList.add("btn-danger");

    const btn = document.getElementById(btn_name);
    btn.classList.remove("btn-danger");
    btn.classList.add("btn-secondary");

    active_btn_name = btn_name;
}

function show_block(blockname) {
    const btn_name = blockname.concat('_button');
    highlight_btn(btn_name);
    const active_block = document.getElementById(active_blockname);
    active_block.classList.add("block_hide");

    const block = document.getElementById(blockname);
    block.classList.remove("block_hide");

    active_blockname = blockname;
}