import telebot
from telebot import types


bot = telebot.TeleBot('1491721360:AAELdxaPLBn2W--cl8SnXowWIA-wJ0qnXms')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Суп ХАРЧО")
    item2 = types.KeyboardButton("Любимый суп")
    item3 = types.KeyboardButton("Шурпа из говядины")
    item4 = types.KeyboardButton("Суп ЗАТИРУХА с курицы")
    item5 = types.KeyboardButton("Томатный суп с курицей, фасолью и овощами")
    item6 = types.KeyboardButton("Сырный суп по‑французски, с курицей")

 
    markup.add(item1, item2, item3, item4, item5, item6)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nДля того чтобы узнать рецепты супов нажми на кнопки или напиши мне название супов. Например: Суп ХАРЧО" 
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    if message.chat.type == 'private':
        if message.text == 'Суп ХАРЧО':
            final_message = f"Суп ХАРЧО\n\nПродукты (на 6 порций):\n\nКурица бройлерная - 1 шт.\nРис - 0,5 стакана\nЧеснок - 1 головка\nМасло сливочное - 50 г\nЛук репчатый - 1 шт.\nМорковь - 1 шт.\nТомат-паста - 2 ст. ложки\nЗелень - 50-60 г\nСоль - 1 ст. ложка"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Любимый суп':
            final_message = f"Любимый суп\n\nПродукты:\n\nКуриный окорочок - 1 шт. (250 г)\nКартофель - 1 шт. (150 г)\nПомидор - 1 шт. (100 г)\nЛук репчатый - 1 шт. (70 г)\nСметана - 2 ст.л. (60 г)\nЗелень укропа и петрушки - 10 г\nМасло растительное для жарки - 1 ст.л.\nСоль - по вкусу\nПерец - по вкусу\nВода - 1,5 л"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Шурпа из говядины':
            final_message = f"Шурпа из говядины\n\nПродукты:\n\nГовядина с косточкой - 800 г\nКартофель - 800 г\nМорковь - 200 г\nЛук - 150 г\nПерец сладкий - 100 г\nЛист лавровый - 3 шт.\nСоль - 1 ст. ложка без горки\nКуркума - 0,5 ч. ложки\nПерец - 0,5 ч. ложки\nКарри - 1 ч. ложка\nЗелень петрушки - 1 пучок"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Суп ЗАТИРУХА с курицы':
            final_message = f"Суп ЗАТИРУХА с курицы\n\nПродукты\n\nКурица (спинка) - 150 г\nЯйца - 2 шт.\nМука - 6 ст. ложек\nКартофель - 2 шт.\nМорковь - 1 шт.\nЛук репчатый - 1 шт.\nЛавровый лист - 1 шт.\nСоль - 0,5 ст. ложки\nПерец чёрный молотый - 1/3 ч. ложки\nМасло растительное - для жарки\nЛук зелёный (по желанию) - для подачи"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Томатный суп с курицей, фасолью и овощами':
            final_message = f"Томатный суп с курицей, фасолью и овощами\n\nПродукты (на 4 порции)\n\nКуриное филе - 300-350 г\nФасоль консервированная - 200 г\nПомидоры в собственном соку - 400 г\nМорковь - 1 шт.\nЛук репчатый - 1 шт.\nПерец болгарский - 1 шт.\nЛук зеленый – 2-4 веточки\nЧеснок - 2 зубчика\nМасло растительное - 2 ст. ложки\nСахар - 1 ч. ложка\nСоль - по вкусу\nПерец черный молотый - 1 щепотка\nПерец красный молотый - 1 щепотка\nПаприка молотая - 1 щепотка\nЛавровый лист - 2-3 шт."
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Сырный суп по‑французски, с курицей':
            final_message = f"Сырный суп по‑французски, с курицей\n\nПродукты (на 6 порций)\n\nФиле куриное - 500 г\nСыр плавленый - 200 г\nКартофель - 400 г\nЛук репчатый - 150 г\nМорковь - 180 г\nМасло сливочное - 30 г\nСоль - по вкусу\nПерец черный молотый - по вкусу\nЗелень - по вкусу"
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_message(message.chat.id, 'Такой суп нету вообще...')


# Это нужно чтобы бот работал
bot.polling(none_stop=True)