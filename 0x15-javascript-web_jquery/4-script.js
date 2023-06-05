const header = $("header");
const redHeader = $("#toggle_header");

redHeader.click(function() {
    header.toggleClass("red green");
});
