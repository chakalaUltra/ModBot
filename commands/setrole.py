import discord
from discord.ext import commands

class SetRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setrole', help='Set a role for a member')
    @commands.has_permissions(manage_roles=True)
    async def setrole(self, ctx, member: discord.Member, *, role):
        role_obj = discord.utils.get(ctx.guild.roles, name=role)
        if role_obj:
            await member.add_roles(role_obj)
            await ctx.send(f'{member} has been given the {role} role')
        else:
            await ctx.send(f'The {role} role does not exist')

def setup(bot):
    bot.add_cog(SetRole(bot))