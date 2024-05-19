from ejercicio18 import ObtenerTotalFactura
nroCliente = int(input("Ingrese el número de cliente "))
total_factura = ObtenerTotalFactura(nroCliente)
print("El total de la factura del cliente nro:",nroCliente,"es de $",total_factura)