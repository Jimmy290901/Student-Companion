// var active_blockname = "#fdp";
// var active_btn_name = "#fdp_button";

// function show_block(blockname) {
//     $(active_blockname).addClass("block_hide");
//     $("#" + blockname).removeClass("block_hide");
//     active_blockname = "#" + blockname;
// }

$("#srchBar").on("keyup",  function() {
    var srchValue = $("#srchBar").val().toUpperCase().split(" ").join("");
    const cards = $(".info-card");
    for (i = 0; i < cards.length; i++) {
        const title = cards[i].innerText.toUpperCase().split(" ").join("");
        if (title.indexOf(srchValue) == -1) {
            cards[i].classList.add("block_hide");
        }
        else {
            cards[i].classList.remove("block_hide");
        }
    }
});