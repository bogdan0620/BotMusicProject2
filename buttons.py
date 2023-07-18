from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def back_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('◀️ Назад')
    kb.add(button)
    return kb


def age_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Зачем нужен возраст?')
    kb.add(button)
    return kb


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttonanswer = KeyboardButton('Как искать?')
    kb.add(buttonanswer)
    return kb


def admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Добавить музыку 📨')
    button_user = KeyboardButton('Список пользователей')
    button_user2 = KeyboardButton('Список возрастов пользователей')
    button2 = KeyboardButton('⏪ Выйти из меню администратора')
    kb.add(button, button_user, button_user2, button2)
    return kb


def main_menu_kb(music_from_db, some='', current_amount=1):
    kb = InlineKeyboardMarkup(row_width=1)

    all_music = reversed([InlineKeyboardButton(text=f'{i[3]} – {i[2]}', callback_data=i[0])
                          for i in music_from_db])

    back_page = InlineKeyboardButton(text='◀️', callback_data='back')
    # pages = (len(all_music) + (-len(all_music) % 10)) // 10
    num_page = InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    next_page = InlineKeyboardButton(text='▶️', callback_data='next')

    if some == 'next':
        new_amount = int(current_amount) + 1

        count = InlineKeyboardButton(text=str(new_amount),
                                     callback_data=str(new_amount))

    elif some == 'back':
        if int(current_amount) > 1:
            new_amount = int(current_amount) - 1

            count = InlineKeyboardButton(text=str(new_amount),
                                         callback_data=str(new_amount))

    kb.add(*all_music)
    kb.row(back_page, num_page, next_page)
    # 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟

    # https://telq.org/question/62bef641b2d5debe9e082d3f
    return kb


def mmm():
    kb = InlineKeyboardMarkup()
    b = InlineKeyboardButton(text='55', callback_data='55')
    kb.add(b)

    return kb
