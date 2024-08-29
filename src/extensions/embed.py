import hikari
import lightbulb

plugin = lightbulb.Plugin("embed")


@plugin.command
@lightbulb.command("embed", "embed stuff idk, don't ask me questions.")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(
        title="Gestalt",
        description="Greater than the sum of its parts.",
        colour=0x5015FF,
        url="https://www.youtube.com/watch?v=wieVdGcOdUc",
    )
    embed.set_author(name="Solaris", url="https://fauux.neocities.org/space",)
    embed.set_image("https://i.pinimg.com/564x/93/b0/2c/93b02c96616ef02dbf57c4661b3ad09d.jpg")
    await ctx.respond(embed=embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
