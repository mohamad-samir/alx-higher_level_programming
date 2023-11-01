// Wait for the document to be ready
$(document).ready(
  function () {
      $('DIV#toggle_header').click(
        function () {
            // Toggle the class to red or green
            if ($('header').hasClass('red')) {
              $('header').removeClass('red');
              $('header').addClass('green');
            } else {
              $('header').removeClass('green');
              $('header').addClass('red');
            }
        });
});
