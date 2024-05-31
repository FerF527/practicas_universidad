def patentesSinDeuda(patentes,deuda):
    patentesSinDeuda = []
    contador = 0
    for patente in patentes:
        if deuda[contador] == 0:
            patentesSinDeuda.append(patente)
        contador += 1
    return patentesSinDeuda


patentes = ["AF238CE", "AC123NE", "AD534FA", "AB871MN"]
deudas = [45725.87, 0, 42711.15, 0]
ProgramaNuevo = patentesSinDeuda(patentes, deudas)
print("Las patentes sin deuda son:",ProgramaNuevo)