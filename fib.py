def fibonacci(n):
  if n <= 1:
    return [0] * n
  else:
    fib_seq = [0, 1]
    for i in range(2, n):
      fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq


# Número a ser verificado
numero = int(input("Digite um número: "))

# Cálculo da sequência de Fibonacci
fib_seq = fibonacci(numero + 1)

# Verificação se o número pertence à sequência
if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


