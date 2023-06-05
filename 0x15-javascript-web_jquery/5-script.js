const addItem = $("#add_item");
const list = $(".my_list");

addItem.click(function() {
    list.append("<li>Item</li>");
});