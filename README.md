# Port-scanner
Port Scanner — это простой инструмент для сканирования открытых портов на заданном хосте.Подходит для задач тестирования сетевой безопасности и изучения основ работы с сетями.

Особенности
🔍 Быстрое сканирование диапазона портов.
⚡ Асинхронное выполнение для повышения скорости.
🛠 Настраиваемый диапазон портов и цели.
✅ Легко запускается в среде Termux или любой системе с установленным Python.
Установка
Зависимости
Для работы требуется Python 3 и Git:

pkg update

pkg upgrade

pkg install python

pkg install git
Клонируйте репозиторий:

git clone https://github.com/wh2te/port-scanner.py

cd port-scanner

python port_scanner.py


Пример ввода:

Введите IP-адрес или доменное имя: 192.168.1.1  
Введите диапазон портов (например, 1-1024): 20-100
Пример результата:
Сканирование хоста 192.168.1.1...
[ОТКРЫТ] Порт 22 на 192.168.1.1
[ОТКРЫТ] Порт 80 на 192.168.1.1
Открытые порты на 192.168.1.1: [22, 80]
