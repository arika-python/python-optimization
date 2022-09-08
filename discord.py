pip install discordwebhook

from discordwebhook import Discord

discord = Discord(url="取得したwebhook urlを記載してください。")
discord.post(content="Hello, world.")