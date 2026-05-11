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