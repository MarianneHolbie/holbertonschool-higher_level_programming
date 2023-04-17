$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (starwarsdata) {
  const episodes = starwarsdata.results;

  for (let i = 0; i < episodes.length; i++) {
    const title = episodes[i].title;
    // construct element to li
    const liElement = `<li>${title}`;
    // append list
    $('UL#list_movies').append(liElement);
  }
});
