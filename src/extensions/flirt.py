import lightbulb

plugin = lightbulb.Plugin("flirt")


@plugin.command
@lightbulb.command("flirt", "Flirts with the user causing massive psychic damage.")
@lightbulb.implements(lightbulb.SlashCommand)
async def flirt(ctx: lightbulb.Context) -> None:
    await ctx.respond("OMG. U r so hot and sexy. <3")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
