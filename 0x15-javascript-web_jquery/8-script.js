// Wait for the document to be ready
$("document").ready(function () {
    // Get the movie titles from the API URL
    const URL = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(URL, function (data) {
        // Update the list in the HTML
        for (const movie of data.results) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        }
    });
});
