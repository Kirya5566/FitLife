# Проект FitLife - MVP версия 1.0

WATER_REC_ML = 30
WATER_ML_1L = 1000
# Узнаем имя пользователя
user_name = input('Добрый день! Введите имя пользователя:')
# Проверка на пустую строку имени
if not user_name:
    raise ValueError('Вы не ввели свое имя!')
try:
    # Сбор данных пользователя возраст, вес, рост
    user_age = int(input('Введите ваш возраст: '))
    user_weight = float(input('Введите ваш вес в кг (пример: 65.5 или 50): '))
    user_height = float(input('Введите ваш рост в м (пример: 1.75 или 2): '))
# Вывод сообщений при ошибке
except ValueError as a:
    error_message = (
        f'{a} Ошибка ввода данных:\n'
        '* Поле не должно быть пустым\n'
        '* Возраст - целое число\n'
        '* Вес - целое или дробное (используй . вместо ,)\n'
        '* Рост - целое или дробное (используй . вместо ,)'
    )
    print(error_message)
else:
    # Проверка для корректности введенных значений и правильного расчета bmi
    if user_age <= 0:
        raise ValueError('Ошибка: возраст должен быть больше 0!')
    if user_weight <= 0:
        raise ValueError('Ошибка: вес должен быть больше 0 кг.')
    if user_height <= 0 or user_height >= 3:
        raise ValueError('Ошибка: рост должен быть больше 0, но меньше 3 м.')
    # Расчетный блок
    bmi = user_weight / (user_height ** 2)  # расчет индекса массы тела
    water_ml = user_weight * WATER_REC_ML  # расчет нормы воды в мл
    water_l = water_ml / WATER_ML_1L  # перевод мл в л
    # Вывод результата
    print(f'\nОтчет для пользователя: {user_name.title()} ({user_age}) г.\n')
    result = (
        f'Твой Индекс Массы Тела: {bmi:.1f}\n'
        f'Рекомендуемая норма воды: {water_l:.1f} л. в день\n'
        'Расчет окончен. Будьте здоровы!'
    )
    print(result)
