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