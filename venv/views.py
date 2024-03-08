from controller import FilmController

film_controller = FilmController()

# добавляем фильмы
film_controller.add_film("Фильм 1", "Режиссер 1", 2022)
film_controller.add_film("Фильм 2", "Режиссер 2", 2023)
film_controller.add_film("Фильм 3", "Режиссер 3", 2024)

# получаем все фильмы и выводим их
all_films = film_controller.get_all_films()

for film in all_films:
    print(f"Название фильма: {film.title} Год выпуска: {film.year} Режиссер: {film.director}")