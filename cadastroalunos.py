alunos = {}

def cadastrar_aluno(matricula, nome, idade, nota):
    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }
    alunos[matricula] = aluno

def cadastrar_aluno_manualmente():
    matricula = int(input("Digite o número de matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    
    cadastrar_aluno(matricula, nome, idade, nota)
    print(f"Aluno com matrícula {matricula} cadastrado com sucesso!")

while True:
    cadastrar_aluno_manualmente()
    continuar = input("Deseja cadastrar outro aluno? (S/N): ").strip().lower()
    if continuar != 's':
        break

print("\nLista de alunos cadastrados:")
for matricula, aluno in alunos.items():
    print(f"Matrícula: {matricula}")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Nota: {aluno['nota']}")
    print("\n")