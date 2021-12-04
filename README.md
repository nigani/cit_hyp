# cit_hyp
Запуск в блокноте Jupiter в Яндекс.DataSphere

Ход решения:
* Изучение данных (блокнот cip-hyper_dst-off.ipynb)
* Разделение тренировочного и тестового датасетов по дням (блокнот 01-split_csv.ipynb)
* Обучение дневных моделей и предсказание результатов по дням  (блокнот 02-random-forest.ipynb)
* Соединение результатов по дням в общий файл resuls.zip (блокнот 03-result_concate.ipynb)
* Применение интсруентария тематического моделирования gensim показано в блокноте 04-gensim.ipynb

Файл results.zip доступен по ссылке
https://drive.google.com/file/d/1uefCPAABvL09n6SURAgolH4DAJTbShgE/view?usp=sharing

В проекте настроен автоматический деплоймент веб-интерфейса на хостинг Heroku через GitHub Actions. После каждого push в репозиторий запускается скрипт, который собирает Streamlit-приложение и выкладывает его на хостинг по адресу https://cithyp.herokuapp.com/
