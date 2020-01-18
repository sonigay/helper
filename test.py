import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jego-972d19158581.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM')

sheet1 = doc.worksheet('시트1')
sheet2 = doc.worksheet('시트2')

client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='재고현황 안내', type=1))




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
    
          
	if message.content.startswith('!재고'):
		SearchID = message.content[len('!재고')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('오전재고').worksheet('시트1')
		
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
            
		embed = discord.Embed(
			title = ' :calling:  ' + SearchID + ' 재고현황! ',
			description= '```' + SearchID + ' 오전까지 내역입니다. ' + result + '실시간조회가 아니라서 다소 차이가 있을수 있습니다. ```',
			color=0xff00ff
			)
		await client.send_message(message.channel, embed=embed)
            
	if message.content.startswith('!모델명'):
		SearchID = message.content[len('!모델명')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('오전재고').worksheet('시트2')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed = discord.Embed(
			title = ' :printer:  모델명 코드 리스트 ',
			description= '```' + SearchID + ' 모델명 코드는 ' + result + ' ```',
			color=0x0000ff
			)
		await client.send_message(message.channel, embed=embed)
                        
access_token = os.environ["BOT_TOKEN"]
git_access_token = os.environ["GIT_TOKEN"]
client.run(access_token)
