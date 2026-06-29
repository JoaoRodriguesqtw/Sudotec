li_distancia = int(input("digite a distancia da viagem: "))
lf_carga = float(input("digite o peso da carga: "))
lf_valor_total = 00.00
li_qtd_pedagios = li_distancia // 80
li_valor_pedagio = li_qtd_pedagios * 15

#estrutura if para calcular o valor da distancia
if 0 < li_distancia <= 100:
  lf_total_frete = li_distancia * 1.50




elif 101 <= li_distancia <= 300:
  lf_total_frete = 150 + (li_distancia - 100) * 1.20



else:
  lf_total_frete = (100 * 1.50) + (200 * 1.20) + ((li_distancia - 300) * 0.90)



#estrutura if para calcular valor de carga
if 0 < lf_carga < 1000:
  lf_total_carga = -(lf_total_frete * 0.1)




elif lf_carga > 5000:
  lf_total_carga = 250.00

else:
  lf_total_carga = 00.00





lf_valor_total =  lf_total_frete + lf_total_carga + li_valor_pedagio


print(f"valor de frete: {(lf_total_frete):.2f} / valor total: {(lf_valor_total):.2f}")

