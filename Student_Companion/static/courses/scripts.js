var active_blockname = "#fdp";
var active_btn_name = "#fdp_button";

function show_block(blockname) {
    $(active_blockname).addClass("block_hide");
    $("#" + blockname).removeClass("block_hide");
    active_blockname = "#" + blockname;
}

$("#fdp #srchBar, #ger #srchBar, #major #srchBar, #elective #srchBar, #complete #srchBar, #incomplete #srchBar").on("keyup",  function() {
    var srchValue = $(active_blockname + " #srchBar").val().toUpperCase().split(" ").join("");
    const cards = $(active_blockname + " .info-card");
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