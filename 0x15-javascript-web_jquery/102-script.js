// Ensure that the page has been fully loaded before executing the code
$(document).ready(function () {
    // When clicking on the button with id `btn_translate`
    $("#btn_translate").click(function () {
        // Fetching the value of the input language code from the element with id `language_code`
        const lang = $("#language_code").val();

        // Building the URL using the language code value
        const URL = `https://www.fourtonfish.com/hellosalut/hello/${lang}`;

        // Using JQuery's API interface to fetch data from the API
        $.get(URL, function (data) {
            // Display the translation in the element with id `hello`
            $("#hello").text(data.hello);
        });
    });
});