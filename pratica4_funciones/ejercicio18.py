# Se desea automatizar el cálculo de la tarifa telefónica para una lista de clientes. La empresa
# informa que cada llamado tiene un costo por conexión más un costo por el tiempo consumido en
# segundos. Se cuenta con las siguientes funciones ya implementadas.
# ObtenerCantidadLlamados(nroCliente): retorna la cantidad de llamados para un cliente.
# ObtenerTiempoPorLlamada(nroCliente, nroLlamada): retorna la cantidad de segundos de un
# llamado de un cliente.
# ObtenerCostoPorLlamada(): retorna el costo fijo por cada llamada.
# ObtenerCostoPorTiempo(seg): retorna el costo de una llamada que dura seg segundos.
# Realizar un programa que indique el monto de la factura para cada cliente.

# retorna la cantidad de llamados para un cliente.
def ObtenerCantidadLlamados(nroCliente) :
    cliente1 = 1
    cliente1Llamados = 2
    if(nroCliente == 1 and cliente1 == 1):
        return cliente1Llamados

# retorna la cantidad de segundos de un llamado de un cliente.
def ObtenerTiempoPorLlamada(nroCliente,nroLlamada):
    cliente1 = 1
    cliente1Llamada1 = 1
    segundosCliente1Llamada1 = 300
    cliente1Llamada2 = 2
    segundosCliente1Llamada2 = 60
    if(nroCliente == cliente1 and nroLlamada == cliente1Llamada1) :
        return segundosCliente1Llamada1
    if(nroCliente == cliente1 and nroLlamada == cliente1Llamada2) :
        return segundosCliente1Llamada2
# retorna el costo fijo por cada llamada.
def ObtenerCostoPorLlamada() :
    costoPorConexion = 20
    return costoPorConexion
# retorna el costo de una llamada que dura seg segundos.
def ObtenerCostoPorTiempo(seg) :
    costoFijoSegundos = 0.9
    costoSegundos = costoFijoSegundos * seg  
    return costoSegundos

# función principal obtener monto de la factura para cada cliente.
def ObtenerTotalFactura(nroCliente) :
    costo_conexion = ObtenerCostoPorLlamada()
    cant_llamados = ObtenerCantidadLlamados(nroCliente)
    for llamada in range(1,cant_llamados + 1) :
        print(llamada)
        if llamada == 1 :
            cant_segundos_llamada1 = ObtenerTiempoPorLlamada(nroCliente,llamada)
            costo_segundos_llamada1 = ObtenerCostoPorTiempo(cant_segundos_llamada1)
        if llamada == 2 :
            cant_segundos_llamada2 = ObtenerTiempoPorLlamada(nroCliente,llamada)
            costo_segundos_llamada2 = ObtenerCostoPorTiempo(cant_segundos_llamada2)
    costo_llamada1 = costo_conexion + costo_segundos_llamada1
    costo_llamada2 = costo_conexion + costo_segundos_llamada2
    total_factura = costo_llamada1 + costo_llamada2
    return total_factura