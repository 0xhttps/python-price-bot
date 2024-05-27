import discord
import dotenv
import os
import requests
import asyncio
from discord import Intents

dotenv.load_dotenv()

client = discord.Client(intents=Intents.default()) 

network = " " #token network
base_url = f'https://api.dexscreener.com/latest/dex/pairs/{network}/' #dex screener URL
addr = '0x**************' #pool address (listed on DexScreener)

async def get_price():
    try:
        response = requests.get(base_url + addr)
        response.raise_for_status()
        data = response.json()
        return {
            "price": data['pair']['priceUsd'],
            "change": f"24h: {data['pair']['priceChange']['h24']}%"
        }
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price (Network Error): {e}')
        return None  
    except KeyError as e:
        print(f'Error parsing price data (KeyError): {e}')
        return None 

async def update_nickname(bot_member, price_data):
    if price_data is None:
        print('Error fetching price data, skipping nickname update.')
        return
    try:
        await bot_member.edit(nick=f'${price_data["price"]}')
        await client.change_presence(activity=discord.CustomActivity(name=price_data["change"]))
    except discord.Forbidden:
        print('Error updating nickname (Missing Permissions)')
    except Exception as e:
        print(f'Unexpected error updating nickname: {e}')

@client.event
async def on_ready():
    print('The bot is ready')

    async def update_status():  
        while True:
            price_data = await get_price()
            for guild in client.guilds:
                try:
                    bot_member = guild.get_member(int(os.getenv('BOT_ID')))
                    if bot_member:
                        await update_nickname(bot_member, price_data)
                        print(f'name updated for guild: {guild.name}')
                    else:
                        print(f'Bot not found in guild: {guild.name}')
                except Exception as e:
                    print(f'Error updating nickname in guild {guild.name}: {e}')
            await asyncio.sleep(30)

    client.loop.create_task(update_status())

client.run(os.getenv('BOT_TOKEN'))