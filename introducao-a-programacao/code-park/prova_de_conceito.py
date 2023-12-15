def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            raise Exception("Não é possivel realizar um Divisão por zero")
    else:
        raise Exception("Operação inválida")


try:
    print(calculadora(3, 0, 4))
except Exception as e:
    print(e)

try:
    print(calculadora(3, 2, 2))
except Exception as e:
    print(e)

try:
    print(calculadora(3, 2, 3))
except Exception as e:
    print(e)

try:
    print(calculadora(3, 2, 4))
except Exception as e:
    print(e)

for args in [(3, 0, 4), (3, 2, 2), (3, 2, 3), (3, 2, 4)]:
    try:
        print(calculadora(*args))
    except Exception as e:
        print(e)


def digite_um_numero_par():
    while True:
        try:
            num = int(input("Digite um número par: "))
            if num % 2 == 0:
                return num
            else:
                print("O número informado não é ímpar")
        except ValueError:
            print("Número inválido")

print(digite_um_numero_par())
