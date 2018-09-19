# Work with Python 3.6
import discord
import uuid
from discord.ext import commands

TOKEN = 'NDkwOTA0NDQ0NjAzNTk2ODAw.DoAGYg.VzPaVrrYWPW7mOhCM1lfDWXg9cY'

client = commands.Bot(command_prefix = '.')
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#SETUP COMMANDS
    if message.content.startswith('.hola'):
        msg = 'Holaaa{0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)
        return

    elif message.content.startswith('.redes'):
            embed = discord.Embed(title="Redes", description="Sígueme en mis redes para enterarte de todo:", color=0x00ff00)
            embed.add_field(name=":space_invader: Twitch", value="https://www.twitch.tv/sysgra", inline=False)
            embed.add_field(name=":bird: Twitter", value="https://twitter.com/sysgrita", inline=False)
            embed.add_field(name=":camera_with_flash: Instagram", value="https://www.instagram.com/systwitch", inline=False)
            await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('.sysgra'):
        embed = discord.Embed(title="🌀 Sysgra", description="Mi amo y señor, Hokage de este nuestro servidor y lider de esta comunidad cada vez más grande. ¡Entra, saluda y unete a nosotros!", color=0x00ff00)
        embed.add_field(name=":space_invader: Twitch", value="https://www.twitch.tv/sysgra", inline=False)
        await client.send_message(message.channel, embed=embed)
        return

    elif message.content.startswith('.staff'):
        #staffId = '<@187211000351555586>'
        #await client.send_message(message.channel, 'Este es un bot custom. Si sabes de algun bug de este, o cualquier '
        #                                          'problema, mencioname o hablame por privado. Sería de agradecer un buen feedback :)'+staffId)
        return

    elif message.content.startswith('.horario'):

        embed = discord.Embed(title=":calendar_spiral: Horario del stream:", description="Horas basadas en la hora local española.", color=0x00ff00)
        embed.add_field(name=":desktop: Entre semana:", value="Tardes: de 20:00 a 00:00", inline=False)
        embed.add_field(name=":desktop: Fines de semana:", value="Mañanas: de 10:00 a 14:00"
                                                       "\nTardes: de 20:00 a 00:00", inline=False)
        await client.send_message(message.channel, embed=embed)

        embed = discord.Embed(title=":bird: Sígueme en Twitter para no perderte nada!",
                              description="https://twitter.com/sysgrita", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
        return


#OTROS COMANDOS

    elif message.content.startswith('.gatito'):
        # Muestra imágenes de gatitos #
        await client.send_message(message.channel, 'http://www.randomkittengenerator.com/cats/rotator.php?'+my_random_string(6))
        return

    elif message.content.startswith('.NARUTO'):
        embed = discord.Embed(title="SASUKE!", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
        await client.send_message(message.channel, 'https://i.ytimg.com/vi/3VG3AL7gfJA/maxresdefault.jpg')
        return
    elif message.content.startswith('.SASUKE'):

        embed = discord.Embed(title="NARUTO!", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
        await client.send_message(message.channel,'https://i.ytimg.com/vi/KfcvtAFaRrY/hqdefault.jpg')
        return










#INSULTOS
'''
    if message.content.startswith('.insulto'):
        #msg = 'Va pallaso 1 pa 1 sin camiseta, que te voy a dar un tiro en la cabeza que ya verás el chaleco donde te va.'.format(message)
        #await client.send_message(message.channel, msg)
        if 'tonto' in message.content:
            msg = 'Y tu un gilipollas, PUM BANEAO'.format(message)
            await client.send_message(message.channel, msg)
            return

        if 'tus muertos' in message.content:
            msg = 'Yo me cago en las cuatro farolas que alumbran a los tuyos'.format(message)
            await client.send_message(message.channel, msg)
            return

        if 'te meto' in message.content:
            if 'hostia' in message.content:
                msg = 'Mira, si te meto yo una hostia morimos los dos, tu de la hostia y yo de la onda expansiva'.format(message)
                await client.send_message(message.channel, msg)
                return
            if 'puñetazo' in message.content:
                msg = 'Como te de yo un puño te dejo hecho bits'.format(message)
                await client.send_message(message.channel, msg)
                return
            if 'navajazo' in message.content:
                msg = 'Y si te meto yo una a ti que? Pues que te dejo hecho bits, pringao'.format(message)
                await client.send_message(message.channel, msg)
                return
            if 'puñalada' in message.content:
                msg = 'Y si te meto yo una a ti que? Pues que te dejo hecho bits, pringao'.format(message)
                await client.send_message(message.channel, msg)
                return
            return

        if 'puta' in message.content:
            if 'madre' in message.content:
                msg = 'La tuya payaso'.format(message)
                await client.send_message(message.channel, msg)
                return
            if 'hijo' in message.content:
                msg = 'ACASO METIME YO CON TU PUTA MADRE?'.format(message)
                await client.send_message(message.channel, msg)
                return
            return
        return
    '''

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

client.run(TOKEN)