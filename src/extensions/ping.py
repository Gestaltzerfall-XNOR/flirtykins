import lightbulb

plugin = lightbulb.Plugin("ping")


@plugin.command
@lightbulb.command("ping", "Checks if bot is sleeping on the job. Pokes with a stick.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("FUCK OFF, I'M HERE.")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
