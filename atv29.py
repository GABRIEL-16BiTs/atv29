def verificar_presenca(alunos_presentes):
    # Contando o número de alunos presentes
    total_alunos = len(alunos_presentes)
    
    # Exibindo a quantidade de alunos e a lista de alunos presentes
    print(f"Alunos presentes: {total_alunos}")
    print(f"Lista de alunos presentes: {', '.join(alunos_presentes)}")
    
    # Verificando se o número de alunos presentes é menor que 5
    if total_alunos < 5:
        print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")

# Exemplo de uso
alunos_presentes = ['Ana', 'Bruno', 'Carlos', 'Daniela']
verificar_presenca(alunos_presentes)
