from discord.ext import commands


class CogUtils:

    @staticmethod
    def get_voice_channel_members(ctx: commands.context.Context):
        author_name = ctx.author.display_name
        user_list = []
        if ctx.message.author.voice is not None:
            user_ids = ctx.message.author.voice.channel.voice_states.keys()
            for user_id in user_ids:
                user_list.append(ctx.guild.get_member(user_id))

        return {
            "author": author_name,
            "users": user_list
        }

    @staticmethod
    def get_member_list(users):
        u = list()
        for user in users["users"]:
            u.append(user.display_name)
        return u
