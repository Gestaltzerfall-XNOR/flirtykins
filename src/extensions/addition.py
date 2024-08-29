import lightbulb

plugin = lightbulb.Plugin("addition")


@plugin.command
@lightbulb.option("second_number", "Enter the second number.", int)
@lightbulb.option("first_number", "Enter the first number.", int)
@lightbulb.command("add", "Adds two numbers to generate sum.")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx: lightbulb.Context) -> None:
    await ctx.respond(
        f"{ctx.options.first_number} + {ctx.options.second_number} = {ctx.options.first_number + ctx.options.second_number}"
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
