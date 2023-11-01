// Wait for the document to be ready
$("document").ready(function () {
    // Update the `character` text
    // Get the name from the API URL
    const URL = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
    $.get(URL, function (data) {
        $("#character").text(data.name);
    });
});
