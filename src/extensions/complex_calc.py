import lightbulb

plugin = lightbulb.Plugin("calculator")


@plugin.command
@lightbulb.option("second_number", "Enter the second number.", float)
@lightbulb.option(
    "operator", "Enter the operator (Valid + - / *)", str, choices=["+", "-", "*", "/"]
)
@lightbulb.option("first_number", "Enter the first number.", float)
@lightbulb.command("calculator", "It calculates. Obviously.")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx: lightbulb.Context) -> None:

    if ctx.options.operator == "+":
        result = ctx.options.first_number + ctx.options.second_number
    elif ctx.options.operator == "-":
        result = ctx.options.first_number - ctx.options.second_number
    elif ctx.options.operator == "/":
        result = ctx.options.first_number / ctx.options.second_number
    if ctx.options.second_number == 0:
        await ctx.respond("Division by zero impossible.")
    elif ctx.options.operator == "*":
        result = ctx.options.first_number * ctx.options.second_number

    await ctx.respond(f"{result}")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
