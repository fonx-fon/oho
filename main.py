import discord
import random

TOKEN = "ODgxODYzMDA5OTUyMjEwOTc1.YSzA7Q.lku4d6LmA9f1JtFr73Qn1bVpMgo"
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def get_members(message):
    users = list()
    if message.author.voice is not None:
        user_ids = list(message.author.voice.channel.voice_states.keys())
        # get user name
        for member in message.guild.members:
            if member.id in user_ids:
                users.append(str(member.name))
    return {
        "author": message.author.name,
        "users": users
    }


def warui(user_data):
    if user_data["users"]:
        random.shuffle(user_data["users"])
        embed = discord.Embed(title="わるいひと",
                              description=user_data["users"][0].replace("エヴァニィ", "**_エヴァニィ_**"),
                              color=discord.Colour.random())
    else:
        embed = discord.Embed(title="わるいひと", description="*%s*" % user_data["author"], color=discord.Colour.gold())
    return embed


def split_members(comment, user_data):
    users = user_data["users"]

    if not users:
        return discord.Embed(title="むり", color=discord.Colour.gold())

    comment_list = comment.split(" ")
    if len(comment_list) < 2:
        return

    team_count = int(comment_list[1])
    ignore_users = None
    target_users = users[:]
    if len(users) > 2:
        ignore_users = comment_list[2:]
        target_users = list(set(users) - set(ignore_users))

    if team_count > len(target_users):
        return

    # shuffle user list
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

    if ignore_users is not None:
        params["description"] = "対象外：%s" % "、".join(ignore_users)

    embed = discord.Embed(**params)
    for team_name, members in teams.items():
        embed.add_field(name="チーム%s" % team_name, value="　" + "、".join(members), inline=False)
    return embed


def comment_help():
    params = {
        "title": "チーム分けBot",
        "description": "チーム分けBotの使い方",
        "color": discord.Colour.random()
    }
    embed = discord.Embed(**params)
    embed.add_field(name="!team n [対象外]", value="ボイスチャンネルに参加して実行します。\n n分チーム分けを行います。")
    embed.add_field(name="!わるいひと", value="わるいひとを決めます。")
    embed.add_field(name="!help", value="ヘルプを表示")
    return embed


# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    try:
        # param valid
        users = get_members(message)
        comment = message.content

        if comment.startswith("!team"):
            embed = split_members(comment, users)
        elif comment.startswith("!help"):
            embed = comment_help()
        elif comment.startswith("!わるいひと"):
            embed = warui(users)
        else:
            return

        if embed is not None:
            await message.channel.send(embed=embed)
    except:
        import traceback
        print(traceback.format_exc())


if __name__ == "__main__":
    client.run(TOKEN)
