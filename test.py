import discord
import asyncio
import random
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
from selenium import webdriver
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
scope1 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #정책시트
creds = ServiceAccountCredentials.from_json_keyfile_name('jego-972d19158581.json', scope)
creds1 = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope1) #정책시트
client = gspread.authorize(creds)
client1 = gspread.authorize(creds1) #정책시트
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM')
doc1 = client1.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI') #정책시트



client = discord.Client()

countG = 0
client = discord.Client()
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="", type=1), afk=False)



@client.event
async def on_message(message):
    global gc #정산
    global creds	#정산
    global channel
    
    if message.content.startswith('!재고'):
        SearchID = message.content[len('!재고')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('영업재고출력')
        wkstime = gc.open('재고관리').worksheet('재고데이터')
        wks.update_acell('A1', SearchID)
        result = wks.acell('B1').value
        result2 = wkstime.acell('A1').value
        result3 = wks.acell('c1').value
        result4 = wks.acell('d1').value
        result5 = wks.acell('e1').value	
        
        embed = discord.Embed(
            title = ' :calling:  ' + SearchID + ' 재고현황! ',
            description= '**```css\n' + SearchID + ' 재고현황 입니다.\n마지막 데이터 업로드시간은\n'+ result2 + ' 입니다.\n' + result + '```**',
            color=0x50508C
            )
        embed2 = discord.Embed(
            title = '',
            description= '**```css\n '+ result3 + '```**',
            color=0x50508C
            )
        embed3 = discord.Embed(
            title = '',
            description= '**```css\n '+ result4 + '```**',
            color=0x50508C
            )	
        embed4 = discord.Embed(
            title = '',
            description= '**```css\n '+ result5 + '실시간조회가 아니라서 다소 차이가 있을수 있습니다. ```**',
            color=0x50508C
            )	
        await message.channel.send(embed=embed)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed4)
	
	
#     if message.content.startswith('!동판'):
#         SearchID = message.content[len('!동판')+1:]
#         gc1 = gspread.authorize(creds1)
#         wks = gc1.open('정책표관리').worksheet('동판출력')
#         wks.update_acell('A1', SearchID)
#         result = wks.acell('B1').value
	
#         embed1 = discord.Embed(
#             title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
#             description= '**```css\n' + SearchID + ' 정책입니다. ' + result + ' ```**',
#             color=0x00ffff
#             )
#         embed2 = discord.Embed(
#             title = ' :globe_with_meridians: 동판 ' + SearchID + ' 정책조회!! ',
#             description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
#             color=0x00ffff
#             )
#         await client.send_message(client.get_channel("674653007132229632"), embed=embed2)
#         await client.send_message(message.channel, embed=embed1)	

    if message.content == '!동판':
        gc1 = gspread.authorize(creds1)		
        wks = gc1.open('정책표관리').worksheet('동판구두2')
        result = wks.acell('au2').value #정책 적용일시
        result1 = wks.acell('C6').value # 광기가동판 TV프리미엄 모바일 신규/MNP
        result2 = wks.acell('D6').value # 광기가동판 TV프리미엄 모바일 재가입/정책기변
        result3 = wks.acell('C7').value # 광기가동판 TV베이직 모바일 신규/MNP
        result4 = wks.acell('D7').value # 광기가동판 TV베이직 모바일 재가입/정책기변
        result5 = wks.acell('C8').value # 광기가동판 TV베이직 모바일 신규/MNP
        result6 = wks.acell('D8').value # 광기가동판 TV베이직 모바일 재가입/정책기변
        result7 = wks.acell('C10').value # 슬림동판 TV프리미엄 모바일 신규/MNP
        result8 = wks.acell('D10').value # 슬림동판 TV프리미엄 모바일 재가입/정책기변
        result9 = wks.acell('C11').value # 슬림동판 TV베이직 모바일 신규/MNP
        result10 = wks.acell('D11').value # 슬림동판 TV베이직 모바일 재가입/정책기변
        result11 = wks.acell('C12').value # 광랜동판 TV프리미엄 모바일 신규/MNP
        result12 = wks.acell('D12').value # 광랜동판 TV프리미엄 모바일 재가입/정책기변
        result13 = wks.acell('C14').value # 광랜동판 TV베이직 모바일 신규/MNP
        result14 = wks.acell('D14').value # 광랜동판 TV베이직 모바일 재가입/정책기변
        result15 = wks.acell('C15').value # 광기가동판 TV베이직 모바일 신규/MNP
        result16 = wks.acell('D15').value # 광기가동판 TV베이직 모바일 재가입/정책기변
        result17 = wks.acell('C16').value # 광기가동판 TV베이직 모바일 신규/MNP
        result18 = wks.acell('D16').value # 광기가동판 TV베이직 모바일 재가입/정책기변
        result19 = wks.acell('AD3').value # 상품권추가
        result20 = wks.acell('AI3').value # IOT추가
        result21 = wks.acell('AK3').value # 셋탑추가
        result22 = wks.acell('AM3').value # TV프리2추가
        result23 = wks.acell('AD6').value # 동판 상품권금액
        result24 = wks.acell('AI6').value # 동판 IOT추가
        result25 = wks.acell('AK6').value # 동판 , 후결합 셋탑추가
        result26 = wks.acell('AM6').value # 동판 TV프리2추가
        result27 = wks.acell('AO3').value # 단독 TV프리2 설명
        result28 = wks.acell('AO6').value # 단독 TV프리2 프리미엄
        result29 = wks.acell('AO7').value # 단독 TV프리2 설명
        result30 = wks.acell('AU3').value # 단독 TV프리2 설명
        result31 = wks.acell('AU6').value # 단독 TV프리2 설명
        result32 = wks.acell('As3').value # 안정화
        result33 = wks.acell('As6').value # 안정화
        result34 = wks.acell('c9').value # 광기가동판 모바일 신규/MNP
        result35 = wks.acell('d9').value # 광기가동판 모바일 재가입/정책기변			
        result36 = wks.acell('c13').value # 슬림동판 모바일 신규/MNP			
        result37 = wks.acell('d13').value # 슬림동판 모바일 재가입/정책기변			
        result38 = wks.acell('c17').value # 광랜동판 모바일 신규/MNP			
        result39 = wks.acell('d17').value # 광랜동판 모바일 재가입/정책기변	
	
        embed = discord.Embed(
                title='🌐 유선 동판 정책',
                description= '```정책 적용 일시내 모바일 개통 및 설치, 결합시 적용```',
                color=0x00ffff
        )
        embed.add_field(
                name="⌛ 정책 적용 일시",
                value='```' + result + '```',
                inline = False
        )
        embed.add_field(
                name="📍 유의사항",
                value='```diff\n-■ 본사 사은품은 3년약정 동판시 지급\n-■ 소호 동판은 개인사업자만 가능(법인 결합 불가)\n-■ (정상요금8회) 미만 요금 납부 후 해지시 수수료 환수\n-■ 해지후 재가입시 수수료 전액 환수\n-  (동일장소 재설치및 가족명의 등)```',
                inline = False
        )
        embed.add_field(
        name= result19,
        value='```' + result23 + '```',
        inline = False
        )
        embed.add_field(
        name= result20,
        value='```' + result24 + '```',
        inline = False
        )
        embed.add_field(
        name= result21,
        value='```' + result25 + '```',
        inline = False
        )
        embed.add_field(
        name= result22,
        value='```' + result26 + '```',
        inline = False
        )
        embed.add_field(
        name= result27,
        value='```' + result28 +"\n"+ result29 + '```',
        inline = False
        )
        embed.add_field(
        name= result30,
        value='```' + result31 + '```',
        inline = False
        )
        embed.add_field(
        name= result32,
        value='```diff\n' + result33 + '```',
        inline = False
        )			
        embed1 = discord.Embed(
        title='',
        description= '```-------------💚광기가(1기가)-------------```',
        color=0x83ff30
        )
        embed1.add_field(
        name="TV상품",
        value='```💚TV(17↑)```',
        inline = True
        )
        embed1.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result1 + '```',
        inline = True
        )
        embed1.add_field(
        name="모바일(재가입/기변)",
        value='```' + result2 + '```',
        inline = True
        )
        embed1.add_field(
        name="TV상품",
        value='```💚TV(프리미엄)```',
        inline = True
        )
        embed1.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result3 + '```',
        inline = True
        )
        embed1.add_field(
        name="모바일(재가입/기변)",
        value='```' + result4 + '```',
        inline = True
        )
        embed1.add_field(
        name="TV상품",
        value='```💚TV(베이직)```',
        inline = True
        )
        embed1.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result5 + '```',
        inline = True
        )
        embed1.add_field(
        name="모바일(재가입/기변)",
        value='```' + result6 + '```',
        inline = True
        )
        embed1.add_field(
        name="TV상품",
        value='```💚TV(미포함)```',
        inline = True
        )
        embed1.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result34 + '```',
        inline = True
        )
        embed1.add_field(
        name="모바일(재가입/기변)",
        value='```' + result35 + '```',
        inline = True
        )	
        embed2 = discord.Embed(
        title='',
        description= '```-------------💛슬림(500메가)-------------```',
        color=0xf9ff27
        )
        embed2.add_field(
        name="TV상품",
        value='```💛TV(17↑)```',
        inline = True
        )
        embed2.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result7 + '```',
        inline = True
        )
        embed2.add_field(
        name="모바일(재가입/기변)",
        value='```' + result8 + '```',
        inline = True
        )
        embed2.add_field(
        name="TV상품",
        value='```💛TV(프리미엄)```',
        inline = True
        )
        embed2.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result9 + '```',
        inline = True
        )
        embed2.add_field(
        name="모바일(재가입/기변)",
        value='```' + result10 + '```',
        inline = True
        )
        embed2.add_field(
        name="TV상품",
        value='```💛TV(베이직)```',
        inline = True
        )
        embed2.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result11 + '```',
        inline = True
        )
        embed2.add_field(
        name="모바일(재가입/기변)",
        value='```' + result12 + '```',
        inline = True
        )
        embed2.add_field(
        name="TV상품",
        value='```💛TV(미포함)```',
        inline = True
        )
        embed2.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result36 + '```',
        inline = True
        )
        embed2.add_field(
        name="모바일(재가입/기변)",
        value='```' + result37 + '```',
        inline = True
        )	
        embed3 = discord.Embed(
        title='',
        description= '```-------------💙광랜(100메가)-------------```',
        color=0x3862ff
        )
        embed3.add_field(
        name="TV상품",
        value='```💙TV(17↑)```',
        inline = True
        )
        embed3.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result13 + '```',
        inline = True
        )
        embed3.add_field(
        name="모바일(재가입/기변)",
        value='```' + result14 + '```',
        inline = True
        )
        embed3.add_field(
        name="TV상품",
        value='```💙TV(프리미엄)```',
        inline = True
        )
        embed3.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result15 + '```',
        inline = True
        )
        embed3.add_field(
        name="모바일(재가입/기변)",
        value='```' + result16 + '```',
        inline = True
        )
        embed3.add_field(
        name="TV상품",
        value='```💙TV(베이직)```',
        inline = True
        )
        embed3.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result17 + '```',
        inline = True
        )
        embed3.add_field(
        name="모바일(재가입/기변)",
        value='```' + result18 + '```',
        inline = True
        )
        embed3.add_field(
        name="TV상품",
        value='```💙TV(미포함)```',
        inline = True
        )
        embed3.add_field(
        name="모바일( 신규/MNP )",
        value='```' + result38 + '```',
        inline = True
        )
        embed3.add_field(
        name="모바일(재가입/기변)",
        value='```' + result39 + '```',
        inline = True
        )	

        await message.channel.send(embed=embed)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)


#    if message.content == '!후결합동판':
#        gc1 = gspread.authorize(creds1)		
#        wks = gc1.open('정책표관리').worksheet('동판구두2')
#        result0 = wks.acell('au1').value #정책 적용일시
#        result = wks.acell('au2').value #정책 적용일시
#        result1 = wks.acell('h6').value # 광기가동판 TV프리미엄 모바일 신규/MNP
#        result2 = wks.acell('h19').value # 광기가동판 TV프리미엄 모바일 재가입/정책기변
#        result3 = wks.acell('h7').value # 광기가동판 TV베이직 모바일 신규/MNP
#        result4 = wks.acell('h20').value # 광기가동판 TV베이직 모바일 재가입/정책기변
#        result7 = wks.acell('h9').value # 슬림동판 TV프리미엄 모바일 신규/MNP
#        result8 = wks.acell('h22').value # 슬림동판 TV프리미엄 모바일 재가입/정책기변
#        result9 = wks.acell('h10').value # 슬림동판 TV베이직 모바일 신규/MNP
#        result10 = wks.acell('h23').value # 슬림동판 TV베이직 모바일 재가입/정책기변
#        result13 = wks.acell('h12').value # 광랜동판 TV프리미엄 모바일 신규/MNP
#        result14 = wks.acell('h25').value # 광랜동판 TV프리미엄 모바일 재가입/정책기변
#        result15 = wks.acell('h13').value # 광랜동판 TV베이직 모바일 신규/MNP
#        result16 = wks.acell('h26').value # 광랜동판 TV베이직 모바일 재가입/정책기변
#        result17 = wks.acell('AD3').value # 상품권추가
#        result18 = wks.acell('AI3').value # IOT추가
#        result19 = wks.acell('AK3').value # 셋탑추가
#        result20 = wks.acell('AM3').value # TV프리2추가
#        result21 = wks.acell('AD6').value # 동판 상품권금액
#        result22 = wks.acell('AI6').value # 동판 IOT추가
#        result23 = wks.acell('AK6').value # 동판 , 후결합 셋탑추가
#        result24 = wks.acell('AM6').value # 동판 TV프리2추가
#        result25 = wks.acell('AO3').value # 단독 TV프리2 설명
#        result26 = wks.acell('AO6').value # 단독 TV프리2 프리미엄
#        result27 = wks.acell('AO7').value # 단독 TV프리2 설명#
#	
#        embed = discord.Embed(
#                title='🌐 유선 후결합 동판 정책',
#                description= '```정책 적용 일시내 모바일 개통 및 설치, 결합시 적용```',
#                color=0x00ffff
#        )
#        embed.add_field(
#                name="⌛ 유선 적용 일시",
#                value='```' + result + '```',
#                inline = False
#        )
#        embed.add_field(
#                name="⌛ 무선 적용 일시",
#                value='```' + result0 + '```',
#                inline = False
#        )
#        embed.add_field(
#                name="📍 유의사항",
#                value='```diff\n-■ 본사 사은품은 3년약정 동판시 지급\n-■ 소호 동판은 개인사업자만 가능(법인 결합 불가)\n-■ 7회 이하 요금 납부 후 해지시 수수료 환수\n-■ 해지후 재가입시 수수료 전액 환수\n-  (동일장소 재설치및 가족명의 등)```',
#                inline = False
#        )
#        embed.add_field(
#                name= result17,
#                value='```' + result21 + '```',
#                inline = False
#        )
#        embed.add_field(
#                name= result18,
#                value='```' + result22 + '```',
#                inline = False
#        )
#        embed.add_field(
#                name= result19,
#                value='```' + result23 + '```',
#                inline = False
#        )
#        embed.add_field(
#                name= result20,
#                value='```' + result24 + '```',
#                inline = False
#        )
#        embed.add_field(
#                name= result25,
#                value='```' + result26 +"\n"+ result27 + '```',
#                inline = False
#        )
#        embed1 = discord.Embed(
#            title='',
#            description= '```-------------💚광기가(1기가)-------------```',
#            color=0x83ff30
#        )
#        embed1.add_field(
#            name="TV상품",
#            value='```💚TV(프리미엄)```',
#            inline = True
#        )
#        embed1.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result1 + '```',
#            inline = True
#        )
#        embed1.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result2 + '```',
#            inline = True
#        )
#        embed1.add_field(
#            name="TV상품",
#            value='```💚TV(베이직)```',
#            inline = True
#        )
#        embed1.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result3 + '```',
#            inline = True
#        )
#        embed1.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result4 + '```',
#            inline = True
#        )
#        embed2 = discord.Embed(
#            title='',
#            description= '```-------------💛슬림(500메가)-------------```',
#            color=0xf9ff27
#        )
#        embed2.add_field(
#            name="TV상품",
#            value='```💛TV(프리미엄)```',
#            inline = True
#        )
#        embed2.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result7 + '```',
#            inline = True
#        )
#        embed2.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result8 + '```',
#            inline = True
#        )
#        embed2.add_field(
#            name="TV상품",
#            value='```💛TV(베이직)```',
#            inline = True
#        )
#        embed2.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result9 + '```',
#            inline = True
#        )
#        embed2.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result10 + '```',
#            inline = True
#        )
#        embed3 = discord.Embed(
#            title='',
#            description= '```-------------💙광랜(100메가)-------------```',
#            color=0x3862ff
#        )
#        embed3.add_field(
#            name="TV상품",
#            value='```💙TV(프리미엄)```',
#            inline = True
#        )
#        embed3.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result13 + '```',
#            inline = True
#        )
#        embed3.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result14 + '```',
#            inline = True
#        )
#        embed3.add_field(
#            name="TV상품",
#            value='```💙TV(베이직)```',
#            inline = True
#        )
#        embed3.add_field(
#            name="모바일( 신규/MNP )",
#            value='```' + result15 + '```',
#            inline = True
#        )
#        embed3.add_field(
#            name="모바일(재가입/기변)",
#            value='```' + result16 + '```',
#            inline = True
#        )

#        await client.send_message(message.channel, embed=embed)
#        await client.send_message(message.channel, embed=embed1)
#        await client.send_message(message.channel, embed=embed2)
#        await client.send_message(message.channel, embed=embed3)



	
	
    if message.content.startswith('!전월실적'):
        SearchID = message.content[len('!전월실적')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('전월실적출력')
        wks.update_acell('A1', SearchID)
        result = wks.acell('B1').value
        result2 = wks.acell('C1').value
        result3 = wks.acell('D1').value
        result4 = wks.acell('E1').value
        
        embed1 = discord.Embed(
            title = ' 📈 ' + SearchID + ' 전월실적! ',
            description= '**```css\n' + SearchID + '2ND/중고/선불개통제외 전월마감실적 입니다.\n중도 취소발생시 실적에서 차이가 생길수 있습니다.\n'+ result + ' ```**',
            color=0x50508C
            )
        embed2 = discord.Embed(
            title = ' 📈 ' + SearchID + ' 모델통계! ',
            description= '**```css\n' + result2 + '```**',
            color=0x50508C
            )
        embed3 = discord.Embed(
            title = '',
            description= '**```css\n' + result3 + ' ```**',
            color=0x50508C
            )        
        embed4 = discord.Embed(
            title = '',
            description= '**```css\n' + result4 + ' 입니다. 한달동안 고생 많으셨습니다. ```**',
            color=0x50508C
            )
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed4)
        
    if message.content.startswith('!당월실적'):
        SearchID = message.content[len('!당월실적')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('당월실적출력')
        wkstime = gc.open('재고관리').worksheet('당월모바일개통데이터')
        wks.update_acell('A1', SearchID)
        result2 = wkstime.acell('C1').value        
        result = wks.acell('B1').value
        result3 = wks.acell('C1').value
        result4 = wks.acell('D1').value
        result5 = wks.acell('E1').value
        
        embed1 = discord.Embed(
            title = ' 📈 ' + SearchID + ' 당월실적! ',
            description= '**```css\n' + SearchID + '2ND/중고/선불개통제외 당월실적 입니다.\n마지막 데이터 업로드시간은\n'+ result2 + ' 입니다.\n' + result + '```**',
            color=0x50508C
            )
        embed2 = discord.Embed(
            title = ' 📈 ' + SearchID + ' 모델통계! ',
            description= '**```css\n' + result3 + '```**',
            color=0x50508C
            )
        embed3 = discord.Embed(
            title = '',
            description= '**```css\n' + result4 + ' ```**',
            color=0x50508C
            )
        embed4 = discord.Embed(
            title = '',
            description= '**```css\n' + result5 + ' 입니다. 실시간조회가 아니라서 다소 차이가 있습니다.\n이번달도 끝까지 화이팅입니다!! ```**',
            color=0x50508C
            )
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed4)
        
        
    if message.content.startswith('!거래처'):
        SearchID = message.content[len('!거래처')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('거래처코드출력')
        wks.update_acell('A1', SearchID)
        result = wks.acell('B1').value
        result2 = wks.acell('C1').value
        result3 = wks.acell('d1').value
        
        embed = discord.Embed(
            title = ' :printer:  거래처 코드 리스트 ',
            description= '```' + result + ' ```',
            color=0x00Bfff
            )
        embed2 = discord.Embed(
            title = '',
            description= '```' + result2 + ' ```',
            color=0x00Bfff
            )
        embed3 = discord.Embed(
            title = '',
            description= '```' + result3 + ' ```',
            color=0x00Bfff
            )
        await message.channel.send(embed=embed)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)

	
    if message.content.startswith('!담당자'):
        SearchID = message.content[len('!담당자')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('담당자출력')
        wks.update_acell('A1', SearchID)
        result = wks.acell('B1').value
        
        embed = discord.Embed(
            title = '거래처별 담당자 연락처 ',
            description= '```' + result + ' ```',
            color=0x00Bfff
            )
        await message.channel.send(embed=embed)

	
	
        
    if message.content.startswith('!모델명'):
        SearchID = message.content[len('!모델명')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('모델명출력')
        wks.update_acell('A1', SearchID)
        result = wks.acell('B1').value
		
        embed = discord.Embed(
            title = ' :printer:  모델명 코드 리스트 ',
            description= '**```css\n' + SearchID + ' 모델명 코드는 ' + result + '```**',
            color=0x0000ff
            )
        await message.channel.send(embed=embed)    
        
	
    if message.content.startswith('!유심'):
        SearchID = message.content[len('!유심')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('유심출력')
        wkstime = gc.open('재고관리').worksheet('재고데이터')
        wks.update_acell('A1', SearchID)
        result2 = wkstime.acell('a1').value        
        result = wks.acell('B1').value
        result3 = wks.acell('C1').value
        result4 = wks.acell('D1').value
        result5 = wks.acell('E1').value
        
        embed1 = discord.Embed(
            title = ' 📈 ' + SearchID + '유심현황! ',
            description= '**```css\n' + SearchID + '잔여 유심현황 입니다.\n마지막 데이터 업로드시간은\n'+ result2 + ' 입니다.\n' + result + '```**',
            color=0x50508C
            )
        embed2 = discord.Embed(
            title = '',
            description= '**```css\n ' + result3 + ' ```**',
            color=0x50508C
            )
        embed3 = discord.Embed(
            title = '',
            description= '**```css\n ' + result4 + ' ```**',
            color=0x50508C
            )
        embed4 = discord.Embed(
            title = '',
            description= '**```css\n' + result5 + ' 입니다. 실시간조회가 아니라서 다소 차이가 있습니다. ```**',
            color=0x50508C
            )
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed4)  
        
        
    if message.content.startswith('!불량'):
        SearchID = message.content[len('!불량')+1:]
        gc = gspread.authorize(creds)
        wks = gc.open('재고관리').worksheet('불량출력')
        wkstime = gc.open('재고관리').worksheet('재고데이터')
        wks.update_acell('A1', SearchID)
        result2 = wkstime.acell('a1').value        
        result = wks.acell('B1').value
        result3 = wks.acell('C1').value
        result4 = wks.acell('D1').value
        result5 = wks.acell('E1').value
        
        embed1 = discord.Embed(
            title = ' 📈 ' + SearchID + ' !불량현황 ',
            description= '**```css\n' + SearchID + '불량형황 입니다.\n마지막 데이터 업로드시간은\n'+ result2 + ' 입니다.\n' + result + '```**',
            color=0x50508C
            )
        embed2 = discord.Embed(
            title = '',
            description= '**```css\n ' + result3 + ' ```**',
            color=0x50508C
            )
        embed3 = discord.Embed(
            title = '',
            description= '**```css\n ' + result4 + ' ```**',
            color=0x50508C
            )
        embed4 = discord.Embed(
            title = '',
            description= '**```css\n ' + result5 + ' 입니다. 실시간조회가 아니라서 다소 차이가 있습니다. ```**',
            color=0x50508C
            )
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed4)      
        
    
    
    
    







access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
