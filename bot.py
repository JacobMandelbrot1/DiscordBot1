import discord
import responses
from cs50 import SQL
db = SQL("sqlite:///feedback.db")

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA5MTQ3NTE0MjM5NzM5NTA2NQ.GBLuPY.S6TRqmTzfdEaHA3oI_xTKtfJyqf69-e4-xvlmU'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is no running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_reaction_add(reaction, user):
        if str(reaction.emoji) == '👍':
            db.execute("INSERT INTO User (feedback) VALUES(?)", 0)
        if str(reaction.emoji) == '👎':
            db.execute("INSERT INTO User (feedback) VALUES(?)", 1)


    client.run(TOKEN)


