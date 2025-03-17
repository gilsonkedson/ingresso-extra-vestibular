import pandas as pd

enem_result = pd.read_excel("planilhas/resultado_enem.xlsx")
titles_result = pd.read_excel("planilhas/titulos_20220204.xlsx")

merged_df = pd.merge(titles_result, enem_result, on="NOME", suffixes=('_titulos', '_enem'))

merged_df["NOTA_FINAL"] = (0.6 * merged_df["NOTA_enem"]) + (0.4 * merged_df["NOTA_titulos"])

sorted_df = merged_df.sort_values(by="NOTA_FINAL", ascending=False).reset_index(drop=True)

for idx, row in sorted_df.iterrows():
    print(f'Posição {idx+1} - NOME: {row["NOME"]} - NOTA: {round(row["NOTA_FINAL"], 2)}')