# Definindo as partições de memória
# Aqui estamos criando uma lista de dicionários, onde cada dicionário representa uma partição de memória.
# Cada partição tem um ID, um tamanho (em KB), e um status que indica se está ocupada ou não.
particoes = [
    {"id": 1, "tamanho": 1000, "ocupada": False},  # Partição 1 com 1000 KB
    {"id": 2, "tamanho": 2000, "ocupada": False},  # Partição 2 com 2000 KB
    {"id": 3, "tamanho": 3000, "ocupada": False},   # Partição 3 com 3000 KB
    {"id": 4, "tamanho": 500, "ocupada": False}   # Partição 4 com 500 KB
]

# Definindo as tarefas
# As tarefas são os "programas" que precisam ser alocados na memória.
# Cada tarefa tem um ID e um tamanho (em KB).
tarefas = [
    {"id": "A", "tamanho": 1200},  # Tarefa A com 1200 KB
    {"id": "B", "tamanho": 800},   # Tarefa B com 800 KB
    {"id": "C", "tamanho": 2500},   # Tarefa C com 2500 KB
    {"id": "D", "tamanho": 400}   # Tarefa D com 4000 KB
]

# Função que implementa a estratégia de alocação "Primeira Partição Livre"
# Essa função tenta alocar cada tarefa na primeira partição que tiver espaço suficiente.
def primeira_particao_livre(tarefas, particoes):
    for tarefa in tarefas:  # Percorre cada tarefa na lista de tarefas
        alocada = False  # Inicializa a variável que indica se a tarefa foi alocada
        for particao in particoes:  # Percorre cada partição na lista de partições
            # Verifica se a partição não está ocupada e se o tamanho dela é suficiente para a tarefa
            if not particao["ocupada"] and particao["tamanho"] >= tarefa["tamanho"]:
                particao["ocupada"] = True  # Marca a partição como ocupada
                print(f"Tarefa {tarefa['id']} alocada na Partição {particao['id']}")
                alocada = True  # Indica que a tarefa foi alocada
                break  # Sai do loop, pois a tarefa já foi alocada
        if not alocada:
            print(f"Tarefa {tarefa['id']} não pôde ser alocada e está na fila de espera.")
            # Se a tarefa não puder ser alocada em nenhuma partição, ela fica na fila de espera

# Função que implementa a estratégia de alocação "Melhor Partição Livre"
# Essa função tenta alocar cada tarefa na menor partição que tenha espaço suficiente.
def melhor_particao_livre(tarefas, particoes):
    for tarefa in tarefas:  # Percorre cada tarefa na lista de tarefas
        melhor_particao = None  # Inicializa a variável que armazenará a melhor partição encontrada
        for particao in particoes:  # Percorre cada partição na lista de partições
            # Verifica se a partição não está ocupada e se o tamanho dela é suficiente para a tarefa
            if not particao["ocupada"] and particao["tamanho"] >= tarefa["tamanho"]:
                # Verifica se essa é a menor partição encontrada até agora
                if melhor_particao is None or particao["tamanho"] < melhor_particao["tamanho"]:
                    melhor_particao = particao  # Atualiza a melhor partição encontrada
        if melhor_particao:
            melhor_particao["ocupada"] = True  # Marca a melhor partição como ocupada
            print(f"Tarefa {tarefa['id']} alocada na Partição {melhor_particao['id']}")
        else:
            print(f"Tarefa {tarefa['id']} não pôde ser alocada e está na fila de espera.")
            # Se nenhuma partição for suficiente, a tarefa fica na fila de espera

# Testando a alocação com a estratégia "Primeira Partição Livre"
print("Alocação com a Primeira Partição Livre:")
primeira_particao_livre(tarefas, particoes)

# Resetando o estado das partições
# Aqui estamos redefinindo o estado das partições para que possamos testar a segunda estratégia
for particao in particoes:
    particao["ocupada"] = False  # Marcando todas as partições como desocupadas novamente

# Testando a alocação com a estratégia "Melhor Partição Livre"