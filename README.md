# Modelagem-Estatistica

## Dados
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Observações
* Criação de 2 DFs: um para analisar a influencia do tipo de escola (publica ou privada) e outro para ver como o tempo desde que já se formou influencia no resultado (por enquanto nao)
* Tinha botado quem sabe a escolaridade do pai E da mãe. Troquei para quem sabe do pai OU da mãe e perdi 1k indios ao inves de 3k (antes tinha 11k)
* ver numero de indios por estado para ver se é viavel o uso (estado ou regiao?)
* (aparentemente esta ok ate agr)

## Dúvidas
* Professor falou para pegar responsavel com maior escolaridade ao inves de excluir quem nao soubesse a escolaridade de ambos. então tambem peguei quem tem o "maior emprego" entre ambos. OK?
* Tem como usar quem NÂO sabe a escolaridade dos pais? nao tem escrito, mas imagino que nao sabe porque nao chegou a conhecer o pai (ou mae). poderia criar dummies, mas ai aumentaria muito o numero de variaveis... o numero de pessoas que nao sabem a escolaridade do pai é quase 4 vezes o numero de pessoas que nao sabem a escolaridade da mae. talvez um tenha maior impacto que o outro
