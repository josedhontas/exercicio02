# Análise de Latência de Rede (Ping RTT)
## Aluno: José Dhonatas Alves Sales

📘 **Exercício n. 2 de sumarização de dados de medição**  
Este projeto tem como objetivo coletar e analisar a latência de rede (RTT - Round Trip Time) de diferentes tipos de conexão, utilizando ferramentas estatísticas para descrever, comparar e interpretar os dados coletados via `ping`.

---

## Como Executar

### Passo 1: Coleta de Dados

1. Torne o script de coleta executável:
    ```bash
    chmod +x coleta_ping.sh
    ```

2. Execute a coleta de ping para cada tipo de conexão:
    ```bash
    ./coleta_ping.sh CABO
    ./coleta_ping.sh 4G
    ```



### Passo 2: Executar a Análise Estatística

1. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
  

2. Execute o script principal:
    ```bash
        python main.py


O script irá:

* Calcular estatísticas descritivas por tipo de conexão.
* Gerar visualizações (boxplot, histograma, QQ-plot).

---

##  Resultados e Análise

A execução do script `main.py` gerou um conjunto de visualizações e um resumo estatístico que permitem uma análise detalhada do Round Trip Time (RTT) para as conexões do tipo **CABO** e **4G**.

### 1. Análise Descritiva

A tabela abaixo resume as principais métricas estatísticas calculadas para as 100 amostras de RTT de cada conexão:

| Métrica | CABO | 4G |
| :--- | :--- | :--- |
| **Média** | 2.2239 ms | 210.1651 ms |
| **Mediana** | 2.165 ms | 151.0 ms |
| **Moda** | 1.78 ms | 110.0 ms |
| **Desvio Padrão** | 1.0535 | 244.6558 |
| **Variância** | 1.1099 | 59856.51 |
| **Coef. de Variação**| 0.4737 | 1.1641 |
| **Q1 (1º Quartil)** | 1.8075 | 118.5 ms |
| **Q2 (2º Quartil)** | 2.165 ms | 151.0 ms |
| **Q3 (3º Quartil)** | 2.5 ms | 291.5 ms |
| **Dist. Interquartil**| 0.6925 | 173.0 ms |

**Conclusões da Análise Descritiva:**

* **Latência (RTT):** A conexão **4G** apresenta uma latência média (210.1 ms) quase **100 vezes maior** que a da conexão a **CABO** (2.2 ms). A mediana também confirma essa grande disparidade, indicando que o 4G é consistentemente mais lento.
* **Variabilidade e Estabilidade:** O **Desvio Padrão** e a **Variância** da conexão **4G** são ordens de magnitude maiores que os da conexão a **CABO**. Isso indica que a conexão 4G é muito mais instável e imprevisível, com picos de latência significativos. O **Coeficiente de Variação (CV)** maior que 1 para o 4G reforça a alta dispersão dos dados em relação à sua média.

### 2. Análise Gráfica

Os gráficos gerados permitem uma interpretação visual clara das características de cada conexão.

![Análise Gráfica das Conexões](https://i.imgur.com/gK5UjF7.png)

* **Boxplot por Conexão:**
    * O boxplot da conexão a **CABO** é extremamente compacto e próximo de zero, mostrando que 99% dos pings tiveram RTT muito baixo e consistente.
    * Em contraste, o boxplot do **4G** é muito mais "alto" e alongado, ilustrando a alta variabilidade e a maior mediana. O ponto acima do limite superior ("whisker") indica a presença de um *outlier*, um valor de RTT excepcionalmente alto (acima de 800 ms).

* **Distribuição dos RTTs (Histograma):**
    * O histograma confirma que os valores de RTT da conexão a **CABO** estão fortemente concentrados entre 1 e 4 ms.
    * A distribuição do **4G** é assimétrica à direita (*right-skewed*), o que é típico para dados de latência de rede. Isso significa que, embora a maioria dos valores se concentre em uma faixa (em torno de 100-200 ms), ocorrem picos de latência muito elevados que "puxam" a média para cima.

### 3. Verificação de Normalidade e Distribuição de Probabilidade

* **Gráfico QQ-Plot (Normalidade):** Este gráfico compara os quantis dos dados observados com os quantis teóricos de uma Distribuição Normal. Para ambas as conexões, mas de forma muito mais acentuada para o **4G**, os pontos desviam significativamente da linha vermelha de referência.
* **Conclusão sobre a Distribuição:** A análise do QQ-Plot e do histograma assimétrico nos permite concluir que os dados de RTT, especialmente do 4G, **não seguem uma Distribuição Normal**. Uma distribuição de probabilidade mais adequada para modelar este tipo de dado seria a **Log-Normal** ou a **Exponencial**, que lidam melhor com valores assimétricos e estritamente positivos.

### 4. Teste de Média da Diferença entre Conexões

O exercício propõe um teste para a média zero da diferença entre as conexões. Embora o teste estatístico formal (como um Teste T para amostras independentes) não esteja nos resultados gráficos, a análise descritiva e visual é tão conclusiva que podemos inferir o resultado.

Com uma diferença de média de mais de 200 ms e variâncias completamente distintas, a hipótese nula de que a diferença entre as médias é zero seria **fortemente rejeitada** com um altíssimo nível de confiança estatística. Fica evidente que existe uma diferença real e muito significativa no desempenho de latência entre as duas conexões.