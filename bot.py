from discord.ext import commands
import os

INTERNAL_EXTENSIONS = [
    "cogs.shuffle",
    "cogs.etc"
]


class TeamShuffle(commands.Bot):

    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        for cog in INTERNAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except:
                import traceback
                traceback.print_exc()

    async def on_ready(self):
        print("ログインしました")


if __name__ == "__main__":
    bot = TeamShuffle(command_prefix="!")
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
