from .filter import FilterCog

async def setup(bot):
    await bot.add_cog(FilterCog(bot))
