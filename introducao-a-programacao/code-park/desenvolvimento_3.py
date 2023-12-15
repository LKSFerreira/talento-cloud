# 1. Usando o laço de repetição `for`:
print()
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)
print("=============\n")

# 2. Usando o laço de repetição `while`:

andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1
print("=============\n")

# Começando do 20º andar até o 1º andar (em ordem decrescente), pulando o 13º andar. A palavra-chave `continue` é usada para pular a iteração atual do laço e passar para a próxima. No caso do laço `while`, nós decrementamos o valor de `andar` em 1 a cada iteração.
