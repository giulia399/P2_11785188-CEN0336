# Árvore filogenética
arvore = {
    "Filo1": {
        "Classe1": {
            "Ordem1": {
                "Familia1": {},
                "Familia2": {}
            },
            "Ordem2": {
                "Familia3": {
                    "Genero3": {},
                    "Genero4": {}
                }
            }
        },
        "Classe2": {
            "Ordem3": {},
            "Ordem4": {
                "Familia4": {},
                "Familia5": {
                    "Genero1": {},
                    "Genero2": {
                        "Especie1": {},
                        "Especie2": {}
                    }
                }
            }
        }
    }
}

# Função recursiva para contar o número de nós
def contar_nos(arvore):
    # Inicia o contador com 1, pois o nó atual também conta
    total_nos = 1
    
    # Percorre todos os filhos do nó atual
    for chave, subarvore in arvore.items():
        # Chama a função recursivamente para cada subárvore
        total_nos += contar_nos(subarvore)
    
    return total_nos

# Chama a função com a árvore
numero_nos = contar_nos(arvore)
print(f"O número total de nós na árvore é: {numero_nos}")
