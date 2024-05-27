# Discord Bot for Dex Screener Price Updates

This Discord bot updates its nickname and status with the latest price and 24-hour price change of a specified token from Dex Screener. 

## Features

- Fetches the latest price of a specified token from Dex Screener.
- Updates the bot's nickname with the current price.
- Updates the bot's status with the 24-hour price change.

## Requirements

- Python 3.7+
- `discord.py` library
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/discord-price-bot.git
cd discord-price-bot
```

2. Install the required libraries:

```bash
pip install discord.py requests python-dotenv
```

3. Create a .env file in the project directory and add your bot token and bot ID:

```env
BOT_TOKEN=your_discord_bot_token
BOT_ID=your_discord_bot_id
```

## Configuration

- Set the `network` variable to the token network you want to monitor (e.g., `ethereum`, `bsc`, etc.).
- Set the `addr` variable to the pool address of the token listed on Dex Screener.

Example: 

```python
network = "ethereum"
addr = '0xYourTokenAddress'
```

## Running the Bot

Run the bot with the following command:

```bash
python bot.py
```

## Notes

- Ensure the bot has the necessary permissions to change its nickname and update its status in the discord server.
- The bot updates its status every 30 seconds; you can adjust this interval by changing the value in `await asyncio.sleep(30)`.