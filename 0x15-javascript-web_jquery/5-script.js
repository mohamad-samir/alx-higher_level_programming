// Wait for the document to be ready
$(document).ready(
  function () {
      $('DIV#add_item').click(
        function () {
            // Add an <li> element to the list
            $('UL.my_list').append('<li>Item</li>');
        });
});
