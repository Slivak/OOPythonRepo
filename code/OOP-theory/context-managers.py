try:
    # Это менеджер контекста
    with open('file.txt') as f:
        for t in f:
            print(t)
except Exception as e:
    print(e)

# Менеджер контекста автоматически закрывает файл
