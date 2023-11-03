$(document).ready(function () {
    // Function to fetch translation based on the language code entered
    function fetchTranslation() {
        const lang = $("#language_code").val();
        const URL = `https://www.fourtonfish.com/hellosalut/hello/${lang}`;

        $.get(URL, function (data) {
            $("#hello").text(data.hello);
        });
    }

    // Listen for click event on the button
    $("#btn_translate").click(fetchTranslation);

    // Listen for keypress event inside the input field
    $("#language_code").keydown(function (event) {
        // If the pressed key is ENTER (which has a value of 13)
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
