import os

from dotenv import load_dotenv
from discord.ext import commands

from cogs.default import DefaultCog
from cogs.schedule import ScheduleCog
from cogs.guildconfig import GuildConfigCog

from utils import prefix


def main():
    bot = commands.Bot(command_prefix=(prefix.get_cmd_prefix))

    bot.add_cog(DefaultCog(bot))
    bot.add_cog(GuildConfigCog(bot))
    bot.add_cog(ScheduleCog(bot))
    bot.run(os.environ["DISCORD_TOKEN"])

    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    load_dotenv()
    main()
