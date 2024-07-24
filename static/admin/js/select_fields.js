(function ($) {
  $(document).ready(function () {
    var fieldNames = JSON.parse(
      document.getElementById("field-names").textContent
    );

    var fieldSelection = $('<div id="field-selection"></div>');
    fieldNames.forEach(function (field) {
      fieldSelection.append(
        '<label><input type="checkbox" name="_selected_fields" value="' +
          field +
          '">' +
          field +
          "</label><br>"
      );
    });

    $("form#changelist-form").prepend(fieldSelection);
  });
})(django.jQuery);
