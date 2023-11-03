$(document).ready(function () {
    // الدالة التي ستقوم بجلب الترجمة بناءً على كود اللغة المُدخل
    function fetchTranslation() {
        const lang = $("#language_code").val();
        const URL = `https://www.fourtonfish.com/hellosalut/hello/${lang}`;

        $.get(URL, function (data) {
            $("#hello").text(data.hello);
        });
    }

    // الاستماع لحدث النقر على الزر
    $("#btn_translate").click(fetchTranslation);

    // الاستماع لحدث الضغط على المفاتيح داخل حقل الإدخال
    $("#language_code").keydown(function (event) {
        // إذا كان المفتاح المضغوط هو ENTER (والذي يملك القيمة 13)
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
