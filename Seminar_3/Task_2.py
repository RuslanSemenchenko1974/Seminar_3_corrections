""" Реализовать функцию, принимающую несколько параметров, описывающих данные
 пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать
 вывод данных о пользователе одной строкой."""


def data_users(name, surname, born_year, users_town, e_mail, phone_namb):
    print('  '.join([name, surname, born_year, users_town, \
                     e_mail, phone_namb]))


par_name = input('Введите имя : ')
par_surname = input('Введите фамилию : ')
par_born_year = input('Введите год рождения : ')
par_users_town = input('Введите город проживания : ')
par_e_mail = input('Введите e-mail : ')
par_phone_namb = input('Введите телефон : ')
data_users(name=par_name, surname=par_surname, born_year=par_born_year \
           , users_town=par_users_town, e_mail=par_e_mail, \
           phone_namb=par_phone_namb)