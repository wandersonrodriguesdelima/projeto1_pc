import math
import random
import datetime
import statistics
import locale   

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = float(input('Prazo (meses): '))
cdi_anual= float(input('CDI anual %: '))/100
perc_cdb= float(input('Percentual do CDI - CDB (%): '))/100
perc_lci= float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii= float(input('Rentabilidade do FII -  (%): '))/100
meta = float (input('Meta financeira (R$): '))

#conversao CDI
cdi_mensal = math.pow ((1+cdi_anual),1/12) -1
#total investido 
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb),meses))+(aporte * meses )
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido +(lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)
 
 #poupança
taxa_poupanca = 0.005

montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses))+(aporte * meses) 

# FII - simulação estatística

fii_base = capital * math.pow(1 + taxa_fii, meses) + aporte * meses

fii1 = fii_base * (1 + random.uniform(-0.03, 0.03))
fii2 = fii_base * (1 + random.uniform(-0.03, 0.03))
fii3 = fii_base * (1 + random.uniform(-0.03, 0.03))
fii4 = fii_base * (1 + random.uniform(-0.03, 0.03))
fii5 = fii_base * (1 + random.uniform(-0.03, 0.03))

fii_valores = [fii1, fii2, fii3, fii4, fii5]

fii_media = statistics.mean(fii_valores)
fii_mediana = statistics.median(fii_valores)
fii_desvio = statistics.stdev(fii_valores)

# =========================
# DATAS
# =========================
data_simulacao = datetime.date.today()
data_resgate = data_simulacao + datetime.timedelta(days=meses*30)

# =========================
# INDICADOR DE META
# =========================
meta_atingida = (montante_cdb >= meta) or (montante_lci >= meta) or (montante_poupanca >= meta) or (fii_media >= meta)

# =========================
# GRÁFICOS ASCII
# =========================
bloco = '█'
# Cada bloco representa R$ 1000
graf_cdb = bloco * int(montante_cdb // 1000)
graf_lci = bloco * int(montante_lci // 1000)
graf_poupanca = bloco * int(montante_poupanca // 1000)
graf_fii = bloco * int(fii_media // 1000)

# =========================
# RELATÓRIO FINAL
# =========================
print('\n' + '='*40)
print('RELATÓRIO DE SIMULAÇÃO FINANCEIRA')
print('='*40)
print(f'Data da simulação: {data_simulacao.strftime("%d/%m/%Y")}')
print(f'Data estimada de resgate: {data_resgate.strftime("%d/%m/%Y")}')
print(f'Total investido: {locale.currency(total_investido, grouping=True)}\n')

print('--- Valores Finais ---')
print(f'CDB: {locale.currency(montante_cdb, grouping=True)} {graf_cdb}')
print(f'LCI/LCA: {locale.currency(montante_lci, grouping=True)} {graf_lci}')
print(f'Poupança: {locale.currency(montante_poupanca, grouping=True)} {graf_poupanca}')
print(f'FII (média): {locale.currency(fii_media, grouping=True)} {graf_fii}\n')

print('--- Estatísticas do FII ---')
print(f'Média: {locale.currency(fii_media, grouping=True)}')
print(f'Mediana: {locale.currency(fii_mediana, grouping=True)}')
print(f'Desvio padrão: {locale.currency(fii_desvio, grouping=True)}\n')

print(f'Meta financeira atingida? {meta_atingida}')
print('='*40)
