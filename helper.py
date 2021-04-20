import discord

def help():
    e = discord.Embed(title="Ajuda:", description="Comandos do servidor", color=0x5C5CFF)
    e.add_field(name="Prefixo", value="$", inline=False)
    e.add_field(name="jjdiz", value="Frase aleatória do JJ", inline=True)
    e.add_field(name="jjgif", value="GIF aleatório do JJ", inline=True)
    e.add_field(name="equipa", value="Como escolher a tua equipa", inline=True)
    e.set_thumbnail(url="https://i.imgflip.com/e8zws.jpg")
    return e

def team():
    e = discord.Embed(title="Ajuda:", description="Como selecionar a tua equipa", color=0x5C5CFF)
    msg = 'Podes escolher em: <#818253181695164426> reagindo à mensagem que lá está! Caso não esteja podes sugerir essa equipa em <#818247450979991623>'
    e.add_field(name="Solução:", value=msg)
    e.set_thumbnail(url='https://images.beinsports.com/8IWAkq6wDkeRcgfc__H0-3WsLdw=/full-fit-in/1000x0/jorgejesus-cropped_mf95s6t532z419lmkw9hk2t8w.jpg')
    return e