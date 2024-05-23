import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# variaveis para analisar depois: "TP_ANO_CONCLUIU".
# analisar quesões ao inves da redação com o mesmo nivel de dificuldade

df22 = pd.read_csv(r'\Users\b47244\Documents\Nova pasta\MICRODADOS_ENEM_2022.csv',  sep=';',encoding='iso-8859-1', usecols=["NU_ANO","TP_FAIXA_ETARIA","TP_SEXO", "TP_ESTADO_CIVIL",
                                                                                                                          "TP_COR_RACA","TP_ST_CONCLUSAO", "TP_ESCOLA",
                                                                                                                          "NO_MUNICIPIO_PROVA","SG_UF_PROVA",
                                                                                                                          "NU_NOTA_COMP3",
                                                                                                                          "Q001","Q002","Q003","Q004","Q005","Q006","Q022","Q025"]).dropna()

# apenas quem nao zerou a redação
df22 = df22[df22['NU_NOTA_COMP3']!=0]

# apenas quem informou o estado civil
df22 = df22[df22['TP_ESTADO_CIVIL']!=0]
df22 = pd.get_dummies(df22, columns=['TP_ESTADO_CIVIL'], prefix='TP_ESTADO_CIVIL')

# apenas quem declarou a etnia
df22 = df22[df22['TP_COR_RACA']!=0]
df22 = pd.get_dummies(df22, columns=['TP_COR_RACA'], prefix='TP_COR_RACA')

# Masculino = 1 e Feminino = 0
df22['TP_SEXO'] = df22['TP_SEXO'].replace('M',1).replace('F',0)

# apenas pessoas que ja concluiram o ensino medio ou vao concluir no ano da prova
# df22 = df22[(df22['TP_ST_CONCLUSAO'] == 1) | (df22['TP_ST_CONCLUSAO'] == 2)].reset_index(drop=True)
# df22['TP_ST_CONCLUSAO'] = df22['TP_ST_CONCLUSAO']-1

# apenas quem informou o tipo de escola
# df22 = df22[df22['TP_ESCOLA']!=1]
# df22['TP_ESCOLA'] = df22['TP_ESCOLA']-2


# Ao invés de usar os municipios, iremos verificar se o aluno fez a prova em uma capital
capitais = [
    'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 
    'Brasília', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 
    'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 
    'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 
    'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas'
]
regioes = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['GO', 'MT', 'MS', 'DF'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC']
}
df22['CAPITAL'] = df22['NO_MUNICIPIO_PROVA'].apply(lambda x: 1 if x in capitais else 0)
def mapear_regiao(uf):
    for regiao, ufs in regioes.items():
        if uf in ufs:
            return regiao
    return None
df22['Regiao'] = df22['SG_UF_PROVA'].apply(mapear_regiao)

# contagem por raça
contagem = df22[df22['TP_ST_CONCLUSAO']==2]['TP_ESCOLA'].value_counts()
print(contagem)


# distribuição da nota dos índios
# dados_indigenas = df22[df22['TP_COR_RACA'] == 5]

def nota_grupo(dados_grupo, info):
    plt.figure(figsize=(10, 6))
    # sns.kdeplot(dados_grupo['NU_NOTA_COMP3'], bw_adjust=2)
    sns.histplot(dados_grupo['NU_NOTA_COMP3'], bins=10, kde=False)
    plt.title(info)
    plt.xlabel('Nota de Redação')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

# nota_grupo(d1, 'Histograma das Notas de alunos que ja concluiram o ensino medio')
print(df22)

