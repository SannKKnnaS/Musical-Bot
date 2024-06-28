import random

rap = ['Neyim Var Ki', 'Rap God', 'Moonlight', 'Mekanın Sahibi', 'Can Not Hold Us','Airplanes','Güzel Günler','Not Afraid','Bir Derdim Var','Same Love','Benden Bu Kadar','Good Feeling','Serinlet Beni','One Man Can Change the World','Sagopa Kajmer - Pesimist EP 6 Lise Defteri']
türkü = ['Uzun İnce Bir Yoldayım', 'Mihriban', 'Gesi Bağları', 'Hekimoğlu', 'Yemen Türküsü', 'Fikrimin İnce Gülü', 'Sarı Gelin', 'Çanakkale Türküsü', 'Mağusa Limanı', 'Benim Yarim Gelişinden Bellidir', 'Dostum Dostum', 'Kara Tren', 'Çökertme', 'Allı Turnam', 'Ne Ağlarsın Benim Zülfü Siyahım']
phonk = ['Shinigami Eyes', 'Yakuza', 'PAIN', 'Zombi', 'Best Friend', 'Slay!', 'TOKYO DRIFT PHONK-REMIX', 'NASH NASH', 'Murder in my Head', 'Close eyes']
soft = ['Imagine', 'Hallelujah', 'Fields of Gold', 'Make You Feel My Love', 'Fast Car', 'Breathe Me', 'Skinny Love', 'The Scientist', 'Your Song', 'Kiss Me', 'A Thousand Years', 'Yellow', 'Someone Like You', 'Landslide', 'I Will Follow You into the Dark']
rock = ['Enter Sandman', 'Bohemian Rhapsody', 'Stairway to Heaven', 'Hotel California', 'Sweet Child O Mine', 'Dibine Kadar', 'Bir Derdim Var', 'Dönence', 'Küllenen Aşk', 'Her Şeyi Yak']
pop =  ['Elini Ver', 'Sezen Aksu', 'Submariner', 'DACİAxYATIYA-Remix', 'Renklensin', 'Kömür', 'Kapalı Kapılar', 'Al 1de Buradan Yak', 'I Like to Way Kiss Me', 'Kehribar', 'Fark Ettim', 'Aşkın Olayım', 'Unutmak Öyle Kolay Mı Sandın', 'Yarım Kalan Sigara']
caz = ['So What', 'Take Five', 'Autumn Leaves', 'All Blues', 'My Favorite Things', 'Feeling Good', 'Blue in Green', 'Fly Me to the Moon', 'Summertime', 'The Girl from Ipanema', 'Watermelon Man', 'Cantaloupe Island', 'Round Midnight', 'Stolen Moments', 'Spain']


import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

import discord

# Intents tanımlaması
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriklerini dinlemek için niyeti etkinleştir

# Client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Info'):
        await message.channel.send("!Rap, !Türkü, !Phonk, !Soft, !Rock, !Pop, !Caz")
    if message.content.startswith('!Rap'):
        await message.channel.send(random.choice(rap))
    if message.content.startswith('!Türkü'):
        await message.channel.send(random.choice(türkü))
    if message.content.startswith('!Phonk'):
        await message.channel.send(random.choice(phonk))
    if message.content.startswith('!Soft'):
        await message.channel.send(random.choice(soft))
    if message.content.startswith('!Rock'):
        await message.channel.send(random.choice(rock))   
    if message.content.startswith('!Pop'):
        await message.channel.send(random.choice(pop)) 
    if message.content.startswith('!Caz'):
        await message.channel.send(random.choice(caz))        
    else:
        await message.channel.send("!Info")

client.run("Bot_Token_In_Here")
