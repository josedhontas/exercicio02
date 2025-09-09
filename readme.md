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
    ```


O script irá:

* Calcular estatísticas descritivas por tipo de conexão.
* Gerar visualizações (boxplot, histograma, QQ-plot).

---

## Resultados da Análise

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

#### Boxplot por Conexão
<img width="751" height="565" alt="image" src="https://github.com/user-attachments/assets/8685c4a1-5286-4242-8025-b02bb8c15601" />

**Análise do Boxplot:**
O gráfico ilustra a enorme diferença de estabilidade. A conexão `CABO` apresenta um RTT baixo e extremamente consistente (boxplot compacto e próximo de zero), enquanto a `4G` possui altíssima variabilidade (boxplot alongado) e a presença de um *outlier* com latência superior a 800 ms.

#### Distribuição dos RTTs (Histograma)
<img width="761" height="572" alt="image" src="https://github.com/user-attachments/assets/5586c291-a39f-4177-8513-bf48f65692d8" />

**Análise do Histograma:**
O histograma confirma que os RTTs da conexão `CABO` estão fortemente concentrados em valores muito baixos (< 5 ms). Em contrapartida, a distribuição do `4G` é **assimétrica à direita** (*right-skewed*), mostrando que, embora haja uma concentração de valores, ocorrem picos de latência muito altos que "puxam" a média para cima.

#### Gráfico QQ-Plot (Verificação de Normalidade)
<img width="568" height="477" alt="image" src="https://github.com/user-attachments/assets/1eaa7f78-ef5c-4db2-9553-a4c548445687" />
<img width="558" height="481" alt="image" src="https://github.com/user-attachments/assets/44340dfc-7264-4754-b0cb-a93225a11ef8" />

**Análise do QQ-Plot:**
Este gráfico compara os dados com uma distribuição normal teórica. Fica evidente que os pontos de ambas as conexões, mas principalmente do `4G`, desviam significativamente da linha de referência. Isso nos permite concluir que os dados de latência **não seguem uma Distribuição Normal**.

---

## Conclusão

A análise conjunta dos dados estatísticos e dos gráficos comprova que a conexão a **CABO é significativamente superior** em latência e estabilidade. A conexão **4G**, nas condições testadas, demonstrou ser não apenas mais lenta, mas também muito mais imprevisível, tornando-a menos adequada para aplicações sensíveis a atrasos, como jogos online ou videoconferências.
