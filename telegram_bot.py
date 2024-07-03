import telegram
import asyncio


TOKEN = '6759448306:AAFN-MXzB4-o5xC-91_ffa0ZQJro0-xazEs'
group_chat_id = -1002057373856
video_path = 'borrar2.mp4'

async def send(chat_id, token):

    try:
        bot = telegram.Bot(token=token)
        #await bot.sendMessage(chat_id, text=msg)
        await bot.sendVideo(chat_id, video_path)
        print('message sent')
    
    except BaseException as e:
        print(e)


asyncio.run(send(group_chat_id, TOKEN))