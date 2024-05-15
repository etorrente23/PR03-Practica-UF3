def calcular_nota_uf2(respuestas):
    nota_por_pregunta = []
    total_puntuadas = sum(respuesta == 'si' for respuesta in respuestas)
    for i, respuesta in enumerate(respuestas):
        if respuesta == 'si':
            nota_por_pregunta.append((f"Pregunta {i+1} -->, 1"))
        else:
            nota_por_pregunta.append((f"Pregunta {i+1} -->, 0"))
    nota_final = total_puntuadas / len(respuestas) * 10
    return nota_final, nota_por_pregunta, total_puntuadas

respuestas_uf2 = []
for i in range(1, 11):
    respuesta = input(f"Pregunta {i}: Has fet aquesta pregunta?: ").lower()
    while respuesta not in ['si', 'no']:
        print("nomes si o no.")
        respuesta = input(f"Pregunta {i}: Has fet aquesta pregunta?: ").lower()
    respuestas_uf2.append(respuesta)

nota_final_uf2, detalles_nota_uf2, preguntas_bien_uf2 = calcular_nota_uf2(respuestas_uf2)

total_preguntas_uf2 = len(respuestas_uf2)
total_preguntas_hechas_uf2 = preguntas_bien_uf2

with open("respostes_uf2.txt", "w") as f:
    f.write("Preguntas UF2:\n")
    for detalle in detalles_nota_uf2:
        f.write(detalle + "\n")
    f.write(f"Nota final sobre 10: {nota_final_uf2}\n")
    f.write(f"Total de preguntas: {total_preguntas_hechas_uf2} de {total_preguntas_uf2}\n")

print("NOTA UF2:")
print(f"Total: {total_preguntas_hechas_uf2} de {total_preguntas_uf2}")
print(f"Nota final sobre 10: {nota_final_uf2}")