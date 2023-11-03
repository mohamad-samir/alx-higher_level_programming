// Ensure that the page has been fully loaded before executing the code
$(document).ready(function () {
    // When clicking on the element with id `add_item`
    $("#add_item").click(function () {
        // Add a new item to the list with class `my_list`
        $("ul.my_list").append("<li>Item</li>");
    });

    // When clicking on the element with id `remove_item`
    $("#remove_item").click(function () {
        // Remove the last item from the list with class `my_list`
        $("ul.my_list li:last").remove();
    });

    // When clicking on the element with id `clear_list`
    $("#clear_list").click(function () {
        // Remove all items from the list with class `my_list`
        $("ul.my_list").empty();
    });
});