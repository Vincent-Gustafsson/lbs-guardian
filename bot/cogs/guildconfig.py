from discord.ext import commands
from discord.ext.commands.core import has_permissions

from utils import prefix


class GuildConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        prefix.set_prefix(guild.id, "!")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        prefix.remove_guild_prefix(guild.id)

    @commands.command()
    @has_permissions(administrator=True)
    async def changeprefix(self, ctx, new_prefix):
        could_set_prefix = prefix.set_prefix(ctx.message.guild.id, new_prefix)

        if not could_set_prefix:
            await ctx.reply("Prefix should not be longer than 3 characters.")
            return

        nickname = new_prefix + " LBS Guardian"
        await ctx.message.guild.me.edit(nick=nickname)
        await ctx.reply(f'Changed prefix to "{new_prefix}"')
