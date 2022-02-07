import pandas as pd

enem_result = pd.read_excel("planilhas/resultado_enem.xlsx")
titles_result = pd.read_excel("planilhas/titulos_20220204.xlsx")
participants = {
    'result': []
}

for x in range(titles_result['NOME'].count()):
    for y in range(enem_result['NOME'].count()):
        if titles_result['NOME'][x] == enem_result['NOME'][y]:
            final_score = (0.6 * enem_result['NOTA'][y]) + (0.4 * titles_result['NOTA'][x])
            participants['result'].append([titles_result['NOME'][x], final_score])
            
def order(participants):
    for passnum in range(len(participants)-1,0,-1):
        for i in range(passnum):
            if participants[i][1]<participants[i+1][1]:
                aux = participants[i]
                participants[i] = participants[i+1]
                participants[i+1] = aux

result = participants['result']
order(result)

for r in range(1, len(result)+1):
    print(f'Posição {r} - NOME: {result[r-1][0]} - NOTA: {round(result[r-1][1], 2)}')