import lightbulb

import hikari

plugin = lightbulb.Plugin("greet")


@plugin.command
@lightbulb.option("user", "Choose a special user to greet! How sweet!", hikari.User)
@lightbulb.command("greet", "Gives a personalized greeting. Hehe.")
@lightbulb.implements(lightbulb.SlashCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(
        f"Hey, {ctx.options.user.mention}, now go fuck yourself.", user_mentions=True
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
