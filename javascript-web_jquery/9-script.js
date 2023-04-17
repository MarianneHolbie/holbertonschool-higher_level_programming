$('document').ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (hellosalut) {
    const value = hellosalut.hello;

    $('DIV#hello').text(value);
  });
});
