const url = "https://swapi-api.hbtn.io/api/films/?format=json";
const movieList = document.querySelector("#list_movies");

fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
      const listItem = document.createElement("li");
      
      listItem.textContent = film.title;
      
      movieList.appendChild(listItem);
    });
  });
