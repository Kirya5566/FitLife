# Проект FitLife - MVP версия 1.0

WATER_REC_ML = 30
WATER_ML_1L = 1000

try:
    # Сбор данных пользователя имя, возраст, вес, рост
    user_name = input('Добрый день! Введите имя пользователя:')
    user_name = user_name.title()
    if not user_name:  # если имя пустое программа вернет ошибку
        raise ValueError
    user_age = int(input('Введите ваш возраст: '))
    user_weight = float(input('Введите ваш вес в кг (пример: 65.5 или 50): '))
    user_height = float(input('Введите ваш рост в м (пример: 1.75 или 2): '))
    # Расчетный блок
    bmi = user_weight / (user_height ** 2)  # расчет индекса массы тела
    water_ml = user_weight * WATER_REC_ML  # расчет нормы воды в мл
    water_l = water_ml / WATER_ML_1L  # перевод мл в л
    # Вывод результата
    print(f'\nОтчет для пользователя: {user_name} ({user_age}) г.')
    print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
    print(f'Рекомендуемая норма воды: {water_l} л. в день')
    print('\nРасчет окончен. Будьте здоровы!')
# Вывод сообщений при ошибке
except (ValueError, ZeroDivisionError):
    print("Ошибка ввода данных. Попробуй заново")
