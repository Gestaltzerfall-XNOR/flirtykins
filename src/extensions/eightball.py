import lightbulb
import random

plugin = lightbulb.Plugin("eightball")


@plugin.command
@lightbulb.option("question", "Your question to ask", True)
@lightbulb.command(
    "eightball", "Grants a totally accurate and reliable fortune. (Results may vary.)"
)
@lightbulb.implements(lightbulb.SlashCommand)
async def eightball(ctx: lightbulb.Context) -> None:
    responses = [
        "Not a fucking chance, kid.",
        "I dunno, I guess.",
        "Hell yeah.",
        "YOU BET YOUR ASS.",
        "lol no.",
        "Try again later, I don't feel like doing anything right now.",
        "guh.",
        "YUUUUUP. Now fuck off.",
        "YES YES YES!",
        "It is fucking inevitable.",
        "FUCK OFF. THE ANSWER IS NO.",
        "Nahhhhhh.",
        "Nope. Not in your lifetime.",
        "Yes, but like, 70% yes.",
        "Kinda, maybe, sorta.",
        "It's a definite possibility. Signed an NDA, can't say anything else.",
        "50/50 ngl.",
        "uhhhhhhhhhhhhhhhh.",
        "ERROR.ERROR.ERROR.",
        "Try again when you aren't a loser.",
        "Ask next year.",
    ]
    await ctx.respond(f"{random.choice(responses)}")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
