from discord.ext import commands

from utils import schedule
from utils import shorthands


class ScheduleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=("s", "sc", "sch"))
    async def schedule(self, ctx, uid=None):
        result = schedule.get_schedule(uid=uid, discord_id=ctx.author.id)

        if isinstance(result, str):
            await ctx.reply(result)
            return

        await ctx.reply(file=result)

    @commands.command(aliases=("sm",))
    async def setme(self, ctx, shorthand):
        if not schedule.is_valid_uid(shorthand):
            await ctx.reply('Invalid shorthand.')
            return

        shorthands.set_shorthand(ctx.author.id, shorthand)
        await ctx.reply('Done. Shorthand is set to ' + shorthand)

    @commands.command(aliases=("gm",))
    async def getme(self, ctx):
        if shorthand := shorthands.get_shorthand(ctx.author.id):
            await ctx.reply(f"Your shorthand is {shorthand}.")
            return

        await ctx.reply("You don't have a shorthand.")
