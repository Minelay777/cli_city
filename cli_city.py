import click
import requests

"""
Реализовать функционал получения информации о городе посредством Python.
User Story: 
 При запуске файла пользователь вводит название города, система
возвращает:
 - название города,
 - страну,
 - валюту 
 - количество населения.
 Tech Requirements:
Ввод реализовать с помощью CLI интерфейса. Выбор WEB-API для получения
информации - на усмотрение разработчика.
Код должен быть читаемым, с комментариями и соответствовать принципам DRY,
KISS, YAGNI.
Код должен быть загружен на GitHub или GitLab как отдельный проект с публичным
доступом.
Формат вывода только такой как в примере:

% python3 task.py Kyiv
>
--------------
Kyiv

Ukraine
UAH
4250000
==============

"""

MY_APY_KEY = '1/A0CepAbSbSFXX4jk/lQw==8GpZICsyggRPEkPF'

# city_name = 'gkgkh'


def city_info(city_name: str, MY_APY_KEY: str):
    """
    Функция возвращает информацию о стране, валюте и населению страны по введёному городу
    :param city_name:
    :param MY_APY_KEY:
    :return:
    """
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
    resp_city = requests.get(api_url, headers={'X-Api-Key': MY_APY_KEY})  # запрос информации о городе
    if resp_city.status_code == requests.codes.ok:
        api_url = 'https://api.api-ninjas.com/v1/country?name={}'.format(resp_city.json()[0]['country'])
        resp_country = requests.get(api_url, headers={'X-Api-Key': MY_APY_KEY})  # запрос информации о стране

        if resp_country.status_code == requests.codes.ok:
            print('--------------')
            print(resp_city.json()[0]['name'])
            print("")
            print(resp_country.json()[0]['name'])
            print(resp_country.json()[0]['currency']['code'])
            print(int(resp_country.json()[0]['population']) * 1000)  # преобразуем в число и переводим в млн. человек
            print('==============')
        else:
            print("Error:", resp_country.status_code, resp_country.text)
    else:
        print(f"Error: invalid city name. {city_name}", resp_city.status_code, resp_city.text)


@click.command()  # подключаем возможность передачи данных из терминала
@click.argument('city_name')  # передаём в качестве аргумента название города, в терминале
# @click.option(help='After space input city name, like Kyiv')
def main(city_name: str, api_key=MY_APY_KEY):
    """
    input city name, like Kyiv and
    return: information of city: country, population, currency code.
    """
    city_info(city_name, api_key)


if __name__ == "__main__":
    try:
        main()
    except TypeError:
        print("System Error")
        # except SyntaxError:
        print("System Error")
        # except IndexError:
        print(f"Invalid city name")
