print("Bom dia/Boa tarde! Bem-vindo(a) à marcação de consultas.")

# Nome do paciente
nome = input("Para começar, qual o seu nome completo, por favor: ")

# Escolha da especialidade
while True:
    print("\nEscolha uma especialidade:")
    print("1. Clínico Geral")
    print("2. Ginecologia") 
    print("3. Pediatria") 
    print("4. Ortopedia")
    print("5. Dermatologia")
    print("6. Cardiologia")

    escolha = input("Digite o número da especialidade escolhida (1 a 6): ")

    if escolha == "1":
        especialidade = "Clínico Geral"
        break
    elif escolha == "2":
        especialidade = "Ginecologia"
        break
    elif escolha == "3":
        especialidade = "Pediatria"
        break
    elif escolha == "4":
        especialidade = "Ortopedia"
        break
    elif escolha == "5":
        especialidade = "Dermatologia"
        break
    elif escolha == "6":
        especialidade = "Cardiologia"
        break
    else:
        print("Opção inválida! Tente novamente.")

# Preferência por médico
preferencia = input("Você tem preferência por algum médico específico? Digite Sim ou Não: ").strip().lower()

if preferencia == "sim":
    while True:
        print("\nEscolha um(a) médico(a):")
        print("1. Dr. Lucas Almeida")
        print("2. Dr. Rafael Torres") 
        print("3. Dra. Mariana Castro") 
        print("4. Dra. Camila Rocha")

        medico_opcao = input("Digite o número do médico escolhido (1 a 4): ")

        if medico_opcao == "1":
            medico = "Dr. Lucas Almeida"
            break
        elif medico_opcao == "2":
            medico = "Dr. Rafael Torres"
            break
        elif medico_opcao == "3":
            medico = "Dra. Mariana Castro"
            break
        elif medico_opcao == "4":
            medico = "Dra. Camila Rocha"
            break
        else:
            print("Opção inválida! Tente novamente.")
else:
    medico = "Sem preferência"

# Horário da consulta
horario = input("Escolha o horário para consulta. Digite Manhã ou Tarde: ").strip().capitalize()

# Confirmação final
print("\n🗓️ Confirmação de Consulta:")
print(f"{nome}, sua consulta com {medico}, especialista em {especialidade}, está agendada para o período da {horario}.")
print("Sua consulta está agendada. Qualquer dúvida, estamos à disposição!")
print("Obrigado pela preferência! Desejamos uma ótima recuperação e saúde!")
