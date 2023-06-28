def is_polidone(data:str)-> bool:
    if data ==data[::-1]:
        return True
    else:
        return False
print(is_polidone("level"))
print(is_polidone("такси"))
print(is_polidone("лешанаполкеклопанашел"))
