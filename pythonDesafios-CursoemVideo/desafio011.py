prd = float(input('Valor do produto: '))
des = (prd/100)*5
val = prd - des
print('O valor do produto é {}, mas com o desconto de 5%, cai para {:.2f} '.format(prd, val))
