from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция-обработчик для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Отправляем ответ пользователю
    await update.message.reply_text("Привет! Я ваш новый бот. Чем могу помочь?")

# Основная функция для запуска бота
def main():
    # Вставьте свой токен ниже
    token = "7876025147:AAHaGOLsjaiKFxKOVjdyRYP-GbfD83kfPXA"
    
    # Создаем приложение бота
    app = Application.builder().token(token).build()
    
    # Добавляем обработчик для команды /start
    app.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    app.run_polling()

# Запуск функции main, когда скрипт выполняется
if __name__ == "__main__":
    main()
