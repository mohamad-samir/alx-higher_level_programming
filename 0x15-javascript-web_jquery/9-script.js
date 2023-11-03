// Wait until the page is fully loaded
$(document).ready(function () {
  // Fetch the data from the specified URL
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    // Display the "hello" value in the DIV element with the ID "hello"
    $("#hello").text(data.hello);
  });
});
