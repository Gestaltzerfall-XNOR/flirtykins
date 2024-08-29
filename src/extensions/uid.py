import lightbulb

import hikari

plugin = lightbulb.Plugin("uid")


@plugin.command
@lightbulb.option("user", "Whose UID do you wish to find?", hikari.User)
@lightbulb.command("uid", "Grabs the UID of the selected user.")
@lightbulb.implements(lightbulb.SlashCommand)
async def uid(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"{ctx.options.user.id}", user_mentions=True)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
