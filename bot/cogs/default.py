from discord.ext import commands

from utils import prefix
from utils.messaging import send_error_message


class DefaultCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error.__cause__, Exception):
            send_error_message(error)

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            guild_prefix = prefix.get_prefix(message.guild.id)
            await message.reply(f"use {guild_prefix}help")
