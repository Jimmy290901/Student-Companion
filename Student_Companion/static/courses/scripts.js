var active_blockname = "fdp";
var active_btn_name = "fdp_button";

function highlight_btn(btn_name) {
    const active_btn = document.getElementById(active_btn_name);
    active_btn.classList.remove("cat-tab-select");
    active_btn.classList.add("cat-tab-unselect");

    const btn = document.getElementById(btn_name);
    btn.classList.remove("cat-tab-unselect");
    btn.classList.add("cat-tab-select");

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

function srchCourse() {
    const srchBar = document.getElementById("srchBar");
    var srchValue = srchBar.value.toUpperCase().split(" ").join("");
    const cards = document.getElementById(active_blockname).getElementsByClassName("info-card");

    for (i = 0; i < cards.length; i++) {
        const title = cards[i].getElementsByTagName("h3")[0];
        var titleVal = (title.textContent || title.innerText).split(" ").join("");
        // console.log(titleVal);
        if (titleVal.toUpperCase().indexOf(srchValue) == -1) {
            cards[i].classList.add("block_hide");
        }
        else {
            cards[i].classList.remove("block_hide");
        }
    }
}
