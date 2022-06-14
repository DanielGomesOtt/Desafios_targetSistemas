sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros

sp = (sp * 100)/total
rj = (rj * 100)/total
mg = (mg * 100)/total
es = (es * 100)/total
outros = (outros * 100)/total

print("Percentual de representação de cada Estado:")
print(f"SP: {round(sp, 2)}%")
print(f"RJ: {round(rj, 2)}%")
print(f"MG: {round(mg, 2)}%")
print(f"ES: {round(es, 2)}%")
print(f"Outros: {round(outros, 2)}%")