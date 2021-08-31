from discord.ext import commands
from discord import Embed, Colour
from cogs.utils import CogUtils
import random
import numpy as np


class Etc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="わるいひと")
    async def warui(self, ctx):
        user = CogUtils.get_voice_channel_members(ctx)
        user_list = CogUtils.get_member_list(user)
        if user["users"]:
            random.shuffle(user_list)
            embed = Embed(title="わるいひと",
                          description=user_list[0],
                          color=Colour.random())
        else:
            embed = Embed(title="わるいひと", description="*%s*" % user["author"], color=Colour.gold())
        await ctx.send(embed=embed)

    @commands.command(name="おれは悪くない")
    async def warukunai(self, ctx):
        user = CogUtils.get_voice_channel_members(ctx)
        s = np.random.choice(["おほっほ～",
                              "めっちゃすっきゃねん",
                              "めっちゃわるいねん",
                              "わるいねん",
                              "わるくないねん"],
                             p=[
                                 0.001,
                                 0.01,
                                 0.1,
                                 0.389,
                                 0.5
                             ])
        embed = Embed(title="おれは悪くない",
                      description="%sは%s" % (user["author"], s),
                      color=Colour.random())
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Etc(bot))
