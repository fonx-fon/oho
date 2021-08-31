from discord.ext import commands
from cogs.utils import CogUtils
import random
import discord


class Shuffle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def team(self, ctx, num, *ignore_members):
        try:
            team_count = int(num)
        except ValueError:
            return

        users = CogUtils.get_voice_channel_members(ctx)
        target_users = CogUtils.get_member_list(users)
        before_len = len(target_users)
        after_len = len(target_users)
        if ignore_members:
            target_users = list(set(target_users) - set(ignore_members))
            after_len = len(target_users)
        ignore = before_len != after_len

        if team_count > len(target_users):
            return

        random.shuffle(target_users)

        i = 1
        teams = dict()
        for user in target_users:
            if str(i) not in teams:
                teams[str(i)] = list()
            ls = teams[str(i)]
            ls.append(user)
            teams[str(i)] = ls

            if i % team_count == 0:
                i = 1
            else:
                i += 1
        params = {
            "title": "チーム分け結果",
            "color": discord.Colour.random()
        }

        if ignore:
            params["description"] = "対象外：%s" % "、".join(ignore_members)

        embed = discord.Embed(**params)
        for team_name, members in teams.items():
            embed.add_field(name="チーム%s" % team_name, value="　" + "、".join(members), inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Shuffle(bot))
