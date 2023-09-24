import discord
import random
from bot_logic import *
from settings import settings


# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Когда бот будет получать сообщение, он будет отправлять в этот же канал какие-то сообщения!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!ping'):
        await message.channel.send('Привет!')
    elif message.content.startswith('!password'):
        await message.channel.send(gen_pass(25))
    elif message.content.startswith('!emodji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('!coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith("!random"):
        await message.channel.send(random_number(1,10))
    elif message.content.startswith("!help"):
        await message.channel.send("Доступные команды:\n!ping - Проверка бота на работоспособность\n!password - Регенерация пароля\n!emodji - Регенерация эмодзи\n!coin - Мини Игра `Орёл или Решка`\n!random - Рандомное число от 1 до 10")
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run(settings["TOKEN"])