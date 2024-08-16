#   Парсер для сайта RialCom
Предстравленный парсер получает на вход код HTML разметки сайта [RialCom.ru](https://www.rialcom.ru/internet_tariffs/) и переводи список тарифов в Excel таблицу. 

Проект написан на python 3.10.4.

## Запуск
1. Проект расположен на [github](https://github.com/Vova675/RialComParser).
2. Использовалось виртуальное окружение __venv__
   ```bash
   python -m venv venv
   ```
3. Зависимости расположены в файле __requirements.txt__
   ```bash
   pip install -r requirements.txt
   ```
4. Конфигурационные параметры расположены в файле __config.py__
   
## Библиотеки
1. beautifulsoup4
2. openpyxl
3. requests
4. regex
   
## Классы
1. Файл __parser\parser.py__ содержит класс __ParserClass__, который используется для считывания данных их HTML разметки
2. Файл __formatters\formatters.py__ содержит классы __InternetApartmentFormatterClass__, __InternetPrivatHouseFormatterClass__, __InternetTVApartmentFormatterClass__, __InternetTVPrivatHouseFormatterClass__, которые отвечают за форматирование полученных парсером данных
3. Файл __excelmaker\excelmaker.py__ содержит класс __ExcelFileMakerClass__, который используется для создание __Excel__ файла

