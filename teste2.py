# Passo 1: Criando o estoque de livros
estoque = [
    "A Jornada do Herói", 
    "Python para Iniciantes", 
    "O Guia do Mochileiro das Galáxias", 
    "O Pequeno Príncipe", 
    "1984", 
    "Dom Casmurro"
]

# Passo 2: Adicionar novos livros
estoque.append("O Hobbit")  # Adiciona "O Hobbit" ao final
estoque.insert(estoque.index("1984") + 1, "A Arte da Guerra")  # Adiciona "A Arte da Guerra" após "1984"

# Passo 3: Remover livros
estoque.remove("Dom Casmurro")  # Remove "Dom Casmurro" do estoque
if "Python para Iniciantes" in estoque:
    estoque.remove("Python para Iniciantes")  # Remove "Python para Iniciantes", se presente

# Passo 4: Ordenação do estoque
estoque.sort()  # Ordena os livros em ordem alfabética
print("Estoque ordenado (alfabético):", estoque)

estoque.sort(reverse=True)  # Ordena os livros em ordem alfabética inversa
print("Estoque ordenado (alfabético inverso):", estoque)

# Passo 5: Alteração de título
estoque[estoque.index("O Pequeno Príncipe")] = "O Pequeno Príncipe - Edição Especial"  # Altera o título

# Passo 6: Contagem de ocorrências
print("O livro 'O Guia do Mochileiro das Galáxias' aparece", estoque.count("O Guia do Mochileiro das Galáxias"), "vezes no estoque.")

# Passo 7: Verificação de presença
print("O livro 'O Hobbit' está no estoque?", "O Hobbit" in estoque)

# Passo 8: Exibição final
print("Estoque final de livros:", estoque)
