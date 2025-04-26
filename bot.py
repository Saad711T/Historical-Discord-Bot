# المكتبات المطلوبة وراح تلاقيها في ملف requirements.txt
import json
import random
import schedule
import time
import asyncio
import discord

TOKEN = '' # اكتب هنا توكن البوت
CHANNEL_ID =00000000   # اكتب هنا رقم الروم

# تحميل بيانات الأعلام من ملف JSON كقاعدة بيانات NoSQL
def load_flags_data(filename="flags.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# نشر علم عشوائي
async def post_random_flag(client):
    flags_data = load_flags_data()
    flag = random.choice(flags_data)
    
    name = flag['name']
    image_url = flag['image_url']
    description = flag['description']
    
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"**{name}**\n{description}\n{image_url}\n\n||By : Saad Almalki / 0xSaad||")
    else:
        print("❌ لم يتم العثور على الروم المطلوب!")

# بوت ديسكورد
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ البوت جاهز باسم {client.user}')
    
    # جدولة المهمة كل 12 ساعة
    async def scheduler():
        while True:
            await post_random_flag(client)
            await asyncio.sleep(12 * 60 * 60)  # 12 ساعة بالثواني

    client.loop.create_task(scheduler())
client.run(TOKEN)
