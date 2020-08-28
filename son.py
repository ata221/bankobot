import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup
import time
from time import ctime
from time import sleep
import os
import feedparser
import urllib.request 

os.system("cls")

client = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix = bot_prefix)

yuzde = [
5,
10,
15,
20,
25,
30,
35,
40,
45,
50,
55,
60,
65,
70,
75,
80,
85,
90,
95,
100
]



@bot.event
async def on_ready():
	print("Bot Online")
	print("İsmim {}".format(bot.user.name))
	print(str(len(set(bot.get_all_members()))) + " Kişiye Hizmet Ediyor!")
	activity = discord.Game(name = "!idda-!kupon")
	await bot.change_presence(status = discord.Status.idle, activity = activity)

@bot.event
async def on_message_delete(message):
	kim = message.author
	mesajicerik = message.content
	print("Silinen mesaj => ", kim, ":", mesajicerik)
	await bot.process_commands(message)
	silinenMesaj = mesajicerik.lower()
	if silinenMesaj == "Mal Bot":
		await message.channel.send("Heh şöyle, Aferin!")

@bot.event
async def on_message(message):
	if message.author != client.user:
		mesaj = message.content.lower()

		if mesaj == "sa":
			await message.channel.send("as")

		elif mesaj == "!dolar":
			dolar_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')
			soup = BeautifulSoup(dolar_kuru.content, "html.parser")
			dolar_fiyat = soup.find("span", {"class":"value up"})
			await message.channel.send("1 Dolar " + dolar_fiyat.text + " TL")

		elif mesaj == "!euro":
			euro_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/euro/')
			soup = BeautifulSoup(euro_kuru.content, "html.parser")
			euro_fiyat = soup.find("span", {"class":"value up"})
			await message.channel.send("1 Euro " + euro_fiyat.text + " TL")
		
		elif mesaj == "!sterlin":
			sterlin_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/sterlin/')
			soup = BeautifulSoup(sterlin_kuru.content, "html.parser")
			sterlin_fiyat = soup.find("span", {"class":"value up"})
			await message.channel.send("1 İngiliz Sterlini " + sterlin_fiyat.text + " TL")

		elif mesaj == "!sigara":
			await message.channel.send(":japanese_goblin: :smoking: :cloud: :cloud: :cloud: :cloud:")
			sleep(2)
			await message.channel.send("Sağlığınız İçin Sigara İçin")

		elif mesaj == "!topluk":
			deger = str(yuzde[random.randint(0, 19)])
			efkar_yuzde = "%" + deger
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " || " + ":ok_hand: " + "Topluk Ölçer " + efkar_yuzde + " Topluk Ölçtü " + ":ok_hand: ")




		elif mesaj == "!idda" or mesaj == "!kupon":
			url = 'https://www.iddaatahmin2.com/iddaa-tahminleri.html'
			r = requests.get(url)
			html = r.text 
			soup = BeautifulSoup(html,"html.parser")
			for tr in soup.find_all('tr')[1]:
				tds = soup.find_all('td')
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[4].text,tds[5].text,tds[6].text))
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[8].text,tds[9].text,tds[10].text))
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[12].text,tds[13].text,tds[14].text))
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[16].text,tds[17].text,tds[18].text))
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[20].text,tds[21].text,tds[22].text))
				await message.channel.send("Takım: %s | Tahmin: %s | Oran: %s\n" % 
					(tds[24].text,tds[25].text,tds[26].text))

				break



			
		
bot.run("NzQ4MTUxMTkxNjQwNDczNzEw.X0ZQGA.RbL3Re_3SvAWjzuhFbl4ONYxvXo") #Tırnakların Arasında Token Olcak