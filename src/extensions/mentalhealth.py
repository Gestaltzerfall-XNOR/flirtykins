import lightbulb

plugin = lightbulb.Plugin("mentalhealth")


@plugin.command
@lightbulb.command("mental_health", "...Are you sure?")
@lightbulb.implements(lightbulb.SlashCommand)
async def mental_health(ctx: lightbulb.Context) -> None:
    await ctx.respond("LOL. Just be normal. Easy. (No refunds.)")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
