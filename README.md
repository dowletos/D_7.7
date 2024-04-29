Проект News Portal


1. Фильтры и пагинация
Добавьте постраничный вывод на /news/, чтобы на одной странице было не больше 10 новостей и были видны номера лишь ближайших страниц, а также возможность перехода к первой или последней странице.

Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости по определённым критериям. Критерии должны быть следующие:

по названию
по имени автора
позже указываемой даты
Убедитесь, что можно выполнить фильтрацию сразу по нескольким критериям.



2. Создание, редактирование и удаление объектов
Запрограммируйте страницы создания, редактирования и удаления новостей и статей. Предлагаем вам расположить страницы по следующим ссылкам:
/news/create/
/news/<int:pk>/edit/
/news/<int:pk>/delete/
/articles/create/
/articles/<int:pk>/edit/
/articles/<int:pk>/delete/
Если вы немного запутались, ввиду того, что модель у нас одна, а страницы под создание статей и новостей должны быть отдельно, то прочитайте подсказку.

При этом не бойтесь сначала поискать информацию в интернете и пробовать разные подходы к решению задачи!