// Wait for the document to be ready
$(document).ready(
  function () {
      $('DIV#red_header').click(
        function () {
            // Add a class `red` to the header element
            $('header').addClass('red');
        });
});
