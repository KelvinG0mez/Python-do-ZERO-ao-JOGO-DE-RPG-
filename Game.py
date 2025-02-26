# Importa a função randint da biblioteca random.
from random import randint

# Lista vazia para armazenar os NPCs (monstros) que serão criados.
lista_npcs = []

# Dicionário que representa o jogador (player) com suas propriedades iniciais.
player = {
    "nome": "Kelvin",  # Nome do jogador
    "level": 1,        # Nível inicial do jogador
    "exp": 0,          # Experiência atual do jogador
    "exp_max": 30,     # Experiência necessária para subir de nível
    "hp": 100,         # Pontos de vida atuais do jogador
    "hp_max": 100,     # Pontos de vida máximos do jogador
    "dano": 25,        # Dano causado pelo jogador
}

# Função para criar um NPC (monstro) com base no nível fornecido.
def criar_npc(level):
    novo_npc = {
        "nome": f"Monstro #{level}",  # Nome do NPC, com base no nível
        "level": level,               # Nível do NPC
        "dano": 5 * level,            # Dano do NPC, proporcional ao nível
        "hp": 100 * level,            # Pontos de vida do NPC, proporcional ao nível
        "hp_max": 100 * level,        # Pontos de vida máximos do NPC
        "exp": 7 * level,             # Experiência que o NPC dá ao ser derrotado
    }
    return novo_npc  # Retorna o NPC criado.

# Função para gerar vários NPCs e adicioná-los à lista de NPCs.
def gerar_npcs(n_npcs):
    for x in range(n_npcs):  # Loop para criar 'n_npcs' NPCs
        npc = criar_npc(x + 1)  # Cria um NPC com nível x + 1
        lista_npcs.append(npc)  # Adiciona o NPC à lista de NPCs

# Função para exibir todos os NPCs da lista.
def exibir_npcs():
    for npc in lista_npcs:  # Loop para percorrer cada NPC na lista
        exibir_npc(npc)     # Chama a função para exibir informações do NPC

# Função para exibir as informações de um NPC específico.
def exibir_npc(npc):
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )

# Função para exibir as informações do jogador.
def exibir_player():
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
    )

# Função para resetar o HP do jogador para o valor máximo.
def reset_player():
    player["hp"] = player["hp_max"]

# Função para resetar o HP de um NPC para o valor máximo.
def reset_npc(npc):
    npc["hp"] = npc["hp_max"]

# Função para verificar se o jogador subiu de nível.
def level_up():
    if player["exp"] >= player["exp_max"]:  # Verifica se a experiência atingiu o máximo
        player["level"] += 1                # Aumenta o nível do jogador
        player["exp"] = 0                   # Zera a experiência atual
        player["exp_max"] = player["exp_max"] * 2  # Dobra a experiência necessária para o próximo nível
        player["hp_max"] += 20              # Aumenta o HP máximo do jogador

# Função para iniciar uma batalha entre o jogador e um NPC.
def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"] > 0:  # Loop enquanto ambos têm HP maior que 0
        atacar_npc(npc)                         # Jogador ataca o NPC
        atacar_player(npc)                      # NPC ataca o jogador
        exibir_info_batalha(npc)                # Exibe informações da batalha

    if player["hp"] > 0:  # Se o jogador venceu
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player["exp"] += npc["exp"]  # Adiciona a experiência do NPC ao jogador
        exibir_player()              # Exibe as informações atualizadas do jogador
    else:  # Se o NPC venceu
        print(f"O {npc['nome']} venceu!")
        exibir_npc(npc)  # Exibe as informações do NPC

    level_up()       # Verifica se o jogador subiu de nível
    reset_player()   # Reseta o HP do jogador
    reset_npc(npc)   # Reseta o HP do NPC

# Função para o jogador atacar o NPC.
def atacar_npc(npc):
    npc["hp"] -= player["dano"]  # Reduz o HP do NPC com base no dano do jogador

# Função para o NPC atacar o jogador.
def atacar_player(npc):
    player["hp"] -= npc["dano"]  # Reduz o HP do jogador com base no dano do NPC

# Função para exibir informações da batalha (HP do jogador e do NPC).
def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print("-----------------\n")

# Gera 5 NPCs e os adiciona à lista de NPCs.
gerar_npcs(5)

# Seleciona o primeiro NPC da lista para batalhar.
npc_selecionado = lista_npcs[0]

# Inicia 5 batalhas com o mesmo NPC (apenas para teste).
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)

# Exibe as informações finais do jogador após as batalhas.
exibir_player()
