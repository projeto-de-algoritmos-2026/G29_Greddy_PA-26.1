class MinHeap:
    def __init__(self):
        self.heap = []

    def __bool__(self):
        return bool(self.heap)

    def ver_raiz(self):
        if not self.heap:
            return None
        return self.heap[0]

    def adicionar(self, item):
        self.heap.append(item)
        self.shift_up(len(self.heap) - 1)

    def remover(self):
        if not self.heap:
            raise IndexError("remover de um heap vazio")
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.shift_down(0)
        return raiz

    def shift_up(self, idx):
        pai_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[pai_idx]:
            self.heap[idx], self.heap[pai_idx] = self.heap[pai_idx], self.heap[idx]
            idx = pai_idx
            pai_idx = (idx - 1) // 2

    def shift_down(self, idx):
        tamanho = len(self.heap)
        while True:
            menor = idx
            filho_esquerdo = 2 * idx + 1
            filho_direito = 2 * idx + 2
            if filho_esquerdo < tamanho and self.heap[filho_esquerdo] < self.heap[menor]:
                menor = filho_esquerdo
            if filho_direito < tamanho and self.heap[filho_direito] < self.heap[menor]:
                menor = filho_direito
            if menor != idx:
                self.heap[idx], self.heap[menor] = self.heap[menor], self.heap[idx]
                idx = menor
            else:
                break

class Reserva:
    def __init__(self, nome: str, inicio: float, fim: float):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim

    def __repr__(self) -> str:
        hora_inicio = self._formatar_hora(self.inicio)
        hora_fim = self._formatar_hora(self.fim)
        return f"[{self.nome}: {hora_inicio} às {hora_fim}]"

    @staticmethod
    def _formatar_hora(tempo: float) -> str:
        horas = int(tempo)
        minutos = int(round((tempo - horas) * 60))
        return f"{horas:02d}:{minutos:02d}"

class GerenciadorDeSala:
    def __init__(self):
        self.solicitacoes: list[Reserva] = []

    def adicionar_solicitacao(self, reserva: Reserva):
        self.solicitacoes.append(reserva)

    def listar_solicitacoes(self):
        if not self.solicitacoes:
            print("Nenhuma aula cadastrada ainda.")
            return False
        print("\n--- Aulas Cadastradas ---")
        for i, req in enumerate(self.solicitacoes):
            print(f"{i} - {req}")
        return True

    def editar_nome(self, indice: int, novo_nome: str):
        if 0 <= indice < len(self.solicitacoes):
            self.solicitacoes[indice].nome = novo_nome
            return True
        return False

    def editar_horario(self, indice: int, novo_inicio: float, novo_fim: float):
        if 0 <= indice < len(self.solicitacoes):
            self.solicitacoes[indice].inicio = novo_inicio
            self.solicitacoes[indice].fim = novo_fim
            return True
        return False

    def excluir_solicitacao(self, indice: int):
        if 0 <= indice < len(self.solicitacoes):
            del self.solicitacoes[indice]
            return True
        return False
    
    def otimizar_sala_unica(self) -> list[Reserva]:
        if not self.solicitacoes:
            return []

        solicitacoes_ordenadas = sorted(self.solicitacoes, key=lambda r: r.fim)
        agenda_aprovada = [solicitacoes_ordenadas[0]]
        ultima_reserva_aprovada = solicitacoes_ordenadas[0]

        for i in range(1, len(solicitacoes_ordenadas)):
            reserva_atual = solicitacoes_ordenadas[i]
            if reserva_atual.inicio >= ultima_reserva_aprovada.fim:
                agenda_aprovada.append(reserva_atual)
                ultima_reserva_aprovada = reserva_atual

        return agenda_aprovada

    def alocar_em_multiplas_salas(self) -> list[list[Reserva]]:
        if not self.solicitacoes:
            return []

        aulas_ordenadas = sorted(self.solicitacoes, key=lambda r: r.inicio)
        salas_heap = MinHeap()
        todas_as_salas = []

        for aula in aulas_ordenadas:
            sala_mais_cedo = salas_heap.ver_raiz()

            if sala_mais_cedo and sala_mais_cedo[0] <= aula.inicio:
                hora_liberacao, indice_sala = salas_heap.remover()
                todas_as_salas[indice_sala].append(aula)
                salas_heap.adicionar((aula.fim, indice_sala))
            else:
                nova_sala_idx = len(todas_as_salas)
                todas_as_salas.append([aula])
                salas_heap.adicionar((aula.fim, nova_sala_idx))

        return todas_as_salas
    
def ler_horario(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite apenas numeros decimais (ex: 14.5).")

if __name__ == "__main__":
    gerenciador = GerenciadorDeSala()
    
    while True:
        print("\n" + "=" * 55)
        print("=== SISTEMA DE RESERVA ===")
        print("1. Adicionar aula")
        print("2. Listar aulas cadastradas")
        print("3. Editar o NOME")
        print("4. Editar os HORARIOS")
        print("5. Excluir aula")
        print("6. Preencher UMA UNICA SALA ao maximo")
        print("7. Alocar TODAS as aulas em MULTIPLAS SALAS")
        print("0. Sair")
        print("=" * 55)
        
        opcao = input("Escolha uma opcao: ").strip()
        
        if opcao == '1':
            nome = input("Nome da materia: ")
            inicio = ler_horario(f"Inicio de {nome} (ex: 8.5): ")
            fim = ler_horario(f"Termino de {nome} (ex: 10.0): ")
            
            if inicio >= fim:
                print("Erro: O termino deve ser depois do inicio.")
            else:
                gerenciador.adicionar_solicitacao(Reserva(nome, inicio, fim))
                print("Aula adicionada com sucesso!")

        elif opcao == '2':
            gerenciador.listar_solicitacoes()

        elif opcao == '3':
            if gerenciador.listar_solicitacoes():
                try:
                    idx = int(input("\nDigite o NUMERO da aula: "))
                    novo_nome = input("NOVO NOME da materia: ")
                    if gerenciador.editar_nome(idx, novo_nome): print("Editado com sucesso!")
                    else: print("Erro: Indice invalido.")
                except ValueError: print("Erro: Digite um numero inteiro.")

        elif opcao == '4':
            if gerenciador.listar_solicitacoes():
                try:
                    idx = int(input("\nDigite o NUMERO da aula: "))
                    inicio = ler_horario("Novo INICIO: ")
                    fim = ler_horario("Novo TERMINO: ")
                    if inicio >= fim: print("Erro: O termino deve ser depois do inicio.")
                    elif gerenciador.editar_horario(idx, inicio, fim): print("Editado com sucesso!")
                    else: print("Erro: Indice invalido.")
                except ValueError: print("Erro: Digite um numero inteiro.")

        elif opcao == '5':
            if gerenciador.listar_solicitacoes():
                try:
                    idx = int(input("\nDigite o NUMERO da aula que deseja excluir: "))
                    if gerenciador.excluir_solicitacao(idx): print("Excluida com sucesso!")
                    else: print("Erro: Indice invalido.")
                except ValueError: print("Erro: Digite um numero inteiro.")

        elif opcao == '6':
            print("\nPREENCHENDO A SALA PRINCIPAL...")
            agenda_unica = gerenciador.otimizar_sala_unica()
            
            if not agenda_unica:
                print("Nenhuma aula cadastrada.")
            else:
                print(f"\nAulas alocadas na Sala 1: {len(agenda_unica)}")
                for aula in agenda_unica:
                    print(f" -> {aula}")
                
                rejeitadas = len(gerenciador.solicitacoes) - len(agenda_unica)
                if rejeitadas > 0:
                    print(f"\n*(Nota: {rejeitadas} aula(s) ficaram sem sala)*")

        elif opcao == '7':
            print("\nCALCULANDO O MINIMO DE SALAS NECESSARIAS...")
            multiplas_salas = gerenciador.alocar_em_multiplas_salas()
            
            if not multiplas_salas:
                print("Nenhuma aula cadastrada.")
            else:
                print(f"\nTotal de salas abertas: {len(multiplas_salas)}\n")
                
                for i, sala in enumerate(multiplas_salas, 1):
                    print(f"--- SALA {i} ---")
                    for aula in sala:
                        print(f" -> {aula}")
                    print() 

        elif opcao == '0':
            print("Saindo do sistema...")
            break
            
        else:
            print("Erro: Opcao invalida. Tente novamente.")