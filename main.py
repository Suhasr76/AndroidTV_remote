import discord
import os
from keep_alive import keep_alive
from python_keypad import print_keyboard
from python_keypad import print_path

keypad_array_1="123+456-789*.0=/"
keypad_array_2="1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+ "
#print("Len of 2 -",len(keypad_array_2))
width_1, height_1=4,4
arr_1 = [[0]*width_1]*height_1
width_2,height_2=7,7
arr_2 = [[0]*width_2]*height_2
temp=0;

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg= message.content
  if msg.startswith('$help'):
    await message.channel.send('1. $layouts \n\t-> All Keyboard layouts')
    await message.channel.send('2. $layout {layout_number}\n\t-> To display specified layout')
    await message.channel.send('2. $path {layout_number}{expression} \n\t-> Shows the shortest path for entering the expression the Android TV Keyboard..')

  if msg.startswith('$path 1'):
    await message.channel.send("generating path\n")
    await message.channel.send(print_path(msg[8:],keypad_array_1,width_1,height_1))

  if msg.startswith('$path 2'):
    await message.channel.send("Generating path\n")
    await message.channel.send(print_path(msg[8:],keypad_array_2,width_2,height_2))  

  
  if msg.startswith('$layouts'):
      await message.channel.send("\nKeyboard Layout 1 ->\n")
      await message.channel.send("-----------------")
      await message.channel.send(print_keyboard(keypad_array_1,arr_1,width_1)) 
      await message.channel.send("-----------------")
      await message.channel.send("\nKeyboard Layout 2 ->\n")
      await message.channel.send("------------------------------")
      await message.channel.send(print_keyboard(keypad_array_2,arr_2,width_2)) 
      await message.channel.send("------------------------------")
  if msg.startswith('$layout 1'):
      await message.channel.send("\nKeyboard Layout 1 ->\n")
      await message.channel.send("-----------------")
      await message.channel.send(print_keyboard(keypad_array_1,arr_1,width_1)) 
      await message.channel.send("-----------------")
  if msg.startswith('$layout 2'):   
      await message.channel.send("\nKeyboard Layout 2 ->\n")
      await message.channel.send("------------------------------")
      await message.channel.send(print_keyboard(keypad_array_2,arr_2,width_2)) 
      await message.channel.send("------------------------------")


  
      

keep_alive()   
client.run(os.getenv('TOKEN'))  