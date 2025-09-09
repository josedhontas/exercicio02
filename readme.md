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

## Resultados e Análise

A análise foi realizada a partir de 100 amostras de RTT (`ping`) de cada tipo de conexão. Os resultados visuais e estatísticos estão consolidados abaixo.

### Gráficos da Análise
*Aqui você deve inserir a sua imagem. Substitua o texto abaixo pela sua imagem.*
![Análise Gráfica das Conexões](URL_DA_SUA_IMAGEM_AQUI.png)

### Resumo Estatístico

| Métrica | CABO | 4G |
| :--- | :--- | :--- |
| **Média** | 2.2239 ms | 210.1651 ms |
| **Mediana** | 2.165 ms | 151.0 ms |
| **Desvio Padrão** | 1.0535 | 244.6558 |
| **Variância** | 1.1099 | 59856.51 |
| **Q1 (1º Quartil)**| 1.8075 | 118.5 ms |
| **Q3 (3º Quartil)**| 2.5 ms | 291.5 ms |

### Conclusões Principais

1.  **Desempenho de Latência:** A conexão a **CABO** é drasticamente mais rápida. Sua latência média (2.22 ms) é quase **100 vezes menor** que a do **4G** (210.16 ms), como evidenciado no **Histograma** e no **Resumo Estatístico**.

2.  **Estabilidade e Previsibilidade:** A conexão **4G** é extremamente instável. O **Desvio Padrão** massivo (244.65) e o **Boxplot** muito alongado mostram uma grande variação nos tempos de resposta, incluindo *outliers* que superam 800 ms. Em contraste, a conexão a **CABO** é altamente consistente e previsível.

3.  **Distribuição dos Dados:** Os gráficos **QQ-Plot** e o **Histograma** assimétrico confirmam que os dados de RTT (especialmente do 4G) **não seguem uma Distribuição Normal**. A distribuição é assimétrica à direita (*right-skewed*), o que é típico em medições de latência.

## Veredito

A análise comprova que existe uma diferença de performance **estatisticamente significativa** entre as duas tecnologias. Para atividades que exigem baixa latência e alta estabilidade (como jogos online, videochamadas ou operações em tempo real), a conexão a **CABO** é indiscutivelmente superior. A conexão **4G**, apesar de funcional, é mais lenta e muito mais suscetível a picos de latência.