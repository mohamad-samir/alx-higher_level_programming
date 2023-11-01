// Wait for the document to be ready
$(document).ready(
  function () {
      $('DIV#update_header').click(
        function () {
            // Update the text of the header
            $('header').text('New get header!!!');
        });
});
