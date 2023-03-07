from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("5970958544:AAFhTMWiNUgjg9U6uNqqLmmw4BS9jt8te0E")  # Bot toekn
ADMINS = env.list("1218525470")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
