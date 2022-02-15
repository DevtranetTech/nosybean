from discord.ext import commands

from exceptions import *


def is_owner():
    """
    This is a custom check to see if the user executing the command is an owner of the guild.
    """

    async def predicate(ctx: commands.Context) -> bool:
        if ctx.author.id != ctx.guild.owner_id:
            raise UserNotOwner
        return True

    return commands.check(predicate)
