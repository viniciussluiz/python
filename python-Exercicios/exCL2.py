import random
confronto1 = ['Napoli', 'Milan']
confronto2 = ['Benfica', 'Inter de Milão']
confronto3 = ['Manchester City', 'Bayern']
confronto4 = ['Real Madrid', 'Chelsea']
time1 = random.sample(confronto1, 1)
time2 = random.sample(confronto2, 1)
time3 = random.sample(confronto3, 1)
time4 = random.sample(confronto4, 1)
print(f'Os confrontos das semifinais serão\n {time1}x{time2}\n {time3}x{time4}')