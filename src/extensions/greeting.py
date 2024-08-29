import lightbulb

plugin = lightbulb.Plugin("greeting")


@plugin.command
@lightbulb.command("greeting", "Greets the user, and maybe more... (;)")
@lightbulb.implements(lightbulb.SlashCommand)
async def greeting(ctx: lightbulb.Context) -> None:
    await ctx.respond(
        "Hey baby cakes. (; I lost my virginity, could I have yours? God, I am sorry. I think my programmer is a bit of an incel."
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
