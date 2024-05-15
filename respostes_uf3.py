def calcular_nota_uf3(respuestas):
    nota_por_pregunta = []
    total_puntuadas = sum(respuesta == 'si' for respuesta in respuestas)
    for i, respuesta in enumerate(respuestas):
        if respuesta == 'si':
            nota_por_pregunta.append((f"Pregunta {i+11} -->, 1"))
        else:
            nota_por_pregunta.append((f"Pregunta {i+11} -->, 0"))
    nota_final = total_puntuadas / len(respuestas) * 10
    return nota_final, nota_por_pregunta, total_puntuadas

respuestas_uf3 = []
for i in range(11, 27):
    respuesta = input(f"Pregunta {i}: Has fet aquesta pregunta?: ").lower()
    while respuesta not in ['si', 'no']:
        print("nomes si o no")
        respuesta = input(f"Pregunta {i}: Has fet aquesta pregunta?: ").lower()
    respuestas_uf3.append(respuesta)

nota_final_uf3, detalles_nota_uf3, preguntas_bien_uf3 = calcular_nota_uf3(respuestas_uf3)

total_preguntas_uf3 = len(respuestas_uf3)
total_preguntas_hechas_uf3 = preguntas_bien_uf3

with open("respostes_uf3.txt", "w") as f:
    f.write("Preguntas UF3:\n")
    for detalle in detalles_nota_uf3:
        f.write(detalle + "\n")
    f.write(f"Nota final sobre 10: {nota_final_uf3}\n")
    f.write(f"Total de preguntas hechas: {total_preguntas_hechas_uf3} de {total_preguntas_uf3}\n")

print("NOTA UF3:")
print(f"Total: {total_preguntas_hechas_uf3} de {total_preguntas_uf3}")
print(f"Nota final sobre 10: {nota_final_uf3}")
