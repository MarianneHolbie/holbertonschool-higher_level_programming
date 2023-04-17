$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (starwarsdata) {
  $('#character').text(starwarsdata.name);
});
