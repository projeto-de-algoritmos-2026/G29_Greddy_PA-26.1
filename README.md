# G29_Greddy_PA-26.1

Número da lista: 29

Conteúdo da disciplina: Interval Scheduling e Interval Partitioning

## Alunos 
| Nome | Matrícula |
|------|-----------|
| Alan Farias Braga | 251005909 |
| Vilmar José Fagundes | 231026590 |

## Sobre

Esse projeto implementa um Sistema de Agendamento e Alocação de Salas baseado em Algoritmos Gulosos (Greedy Algorithms).

A solução do sistema está nas suas funções de geração de cronograma, para resolver dois problemas clássicos de alocação de recursos. Na simulação de uma sala única, o sistema resolve por meio do algorítmo **Interval Scheduling**. O algoritmo garante rigorosamente a maximização do uso do espaço ordenando os pedidos pelo horário de término, escolhendo sempre a próxima atividade compatível que acaba mais cedo, a sala é liberada o mais rápido possível para a próxima demanda.

Já para o desafio de alocar todas as aulas sem rejeições, o sistema resolve por **Interval Partitioning**, em conjunto com uma **Min-Heap**. Nesse contexto, as aulas são ordenadas de forma estritamente cronológica, pelo horário de início. O algoritmo utiliza a Heap para rastrear e ordenar a disponibilidade das salas abertas, garantindo que o espaço físico que ficará vazio mais cedo permaneça sempre no topo da fila, pronto para ser reaproveitado de forma instantânea.

Conforme o sistema processa a lista de aulas, ele compara o início da atividade com o topo da Heap. Se a sala que libera mais rápido já estiver vazia, a aula é alocada e a sala retorna para a Heap atualizada com o seu novo horário de término. Porém, se a aula precisa começar antes dessa sala esvaziar, o algoritmo conclui que todas as outras também estão ocupadas naquele exato instante, forçando automaticamente a abertura de uma nova sala. Esse ciclo contínuo processa todas as pendências em uma única percursão, garantindo a integridade dos horários e entregando a configuração exata do menor número absoluto de salas necessárias para o funcionamento do projeto.

## Screenshot

## Instalação 

## Gravação
