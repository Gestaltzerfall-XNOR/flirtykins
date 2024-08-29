import lightbulb

plugin = lightbulb.Plugin("echo")


@plugin.command
@lightbulb.option("text", "Text to be repeated.", True)
@lightbulb.command("echo", "Your own pet parrot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
