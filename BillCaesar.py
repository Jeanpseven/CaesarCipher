def codificar_cesar(mensagem, chave):
    mensagem_codificada = ""
    for caractere in mensagem:
        if caractere.isalpha():
            if caractere.isupper():
                indice = ord(caractere) - ord('A')
                indice_codificado = (indice + chave) % 26
                caractere_codificado = chr(indice_codificado + ord('A'))
                mensagem_codificada += caractere_codificado
            else:
                indice = ord(caractere) - ord('a')
                indice_codificado = (indice + chave) % 26
                caractere_codificado = chr(indice_codificado + ord('a'))
                mensagem_codificada += caractere_codificado
        else:
            mensagem_codificada += caractere
    return mensagem_codificada

def decodificar_cesar(mensagem_codificada, chave):
    return codificar_cesar(mensagem_codificada, -chave)

# Solicitar ao usuário a opção de codificar ou decodificar
opcao = input("Escolha uma opção (C)odificar ou (D)ecodificar: ").upper()

# Verificar a opção escolhida
if opcao == "C":
    funcao_codificar = codificar_cesar
    funcao_decodificar = decodificar_cesar
elif opcao == "D":
    funcao_codificar = decodificar_cesar
    funcao_decodificar = codificar_cesar
else:
    print("Opção inválida. Encerrando o programa.")
    exit()

# Solicitar ao usuário a mensagem e a chave
mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave numérica ou palavra-chave: ")

# Converter a chave para um número inteiro
if chave.isnumeric():
    chave = int(chave)
else:
    # Converter a chave palavra-chave em um número somando os valores ASCII dos caracteres
    chave = sum(ord(c.lower()) - ord('a') + 1 for c in chave if c.isalpha())

# Codificar ou decodificar a mensagem usando a chave
mensagem_processada = funcao_codificar(mensagem, chave)

# Imprimir o resultado
print("Resultado:", mensagem_processada)
