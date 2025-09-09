import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv("dados_ping.csv")
df["rotulo"] = df["rotulo"].astype(str)
df["tempo_ms"] = df["tempo_ms"].astype(float)

ordem = ["CABO", "FIBRA", "WI-FI", "4G", "5G"]
conexoes = [c for c in ordem if c in df["rotulo"].unique()] or list(df["rotulo"].unique())


def resumo_stats(s):
    s = s.dropna().astype(float)
    media = s.mean()
    q1, q2, q3 = np.percentile(s, [25, 50, 75])
    return {
        "Média": media,
        "Mediana": q2,
        "Moda": s.mode().iloc[0] if not s.mode().empty else np.nan,
        "Variância": s.var(ddof=1),
        "Desvio Padrão": s.std(ddof=1),
        "Coef. Variação": (s.std(ddof=1) / media) if media != 0 else np.nan,
        "Q1": q1, "Q2": q2, "Q3": q3,
        "Dist. Interquartil": q3 - q1,
        "Semi-Interquartil": (q3 - q1) / 2,
        "Desvio Abs. Médio": (np.abs(s - media)).mean(),
        "n": len(s)
    }

resumo = {c: resumo_stats(df.loc[df.rotulo == c, "tempo_ms"]) for c in conexoes}
resumo_df = pd.DataFrame(resumo).T.loc[:, [
    "n","Média","Mediana","Moda","Variância","Desvio Padrão","Coef. Variação",
    "Q1","Q2","Q3","Dist. Interquartil","Semi-Interquartil","Desvio Abs. Médio"
]].round(3)


linhas_testes = []
for c in conexoes:
    serie = df.loc[df.rotulo == c, "tempo_ms"]
    w, p = stats.shapiro(serie)
    linhas_testes.append(f"{c} • Shapiro-Wilk: W={w:.3f}, p={p:.3g}")

if len(conexoes) >= 2:
    a = df.loc[df.rotulo == conexoes[0], "tempo_ms"].values
    b = df.loc[df.rotulo == conexoes[1], "tempo_ms"].values
    if len(a) == len(b):
        t, p = stats.ttest_rel(a, b)
        linhas_testes.append(f"{conexoes[0]} vs {conexoes[1]} • t pareado: t={t:.3f}, p={p:.3g}")
    else:
        t, p = stats.ttest_ind(a, b, equal_var=False)
        linhas_testes.append(f"{conexoes[0]} vs {conexoes[1]} • t Welch: t={t:.3f}, p={p:.3g}")

testes_texto = "\n".join(linhas_testes)

plt.figure(figsize=(8,6))
plt.boxplot([df.loc[df.rotulo == c, "tempo_ms"] for c in conexoes],
            labels=conexoes, showfliers=True)
plt.title("Boxplot por conexão")
plt.ylabel("tempo_ms")
plt.grid(alpha=0.3)
plt.show()


plt.figure(figsize=(8,6))
todos = df["tempo_ms"].values
bins = np.histogram_bin_edges(todos, bins='auto')
for c in conexoes:
    plt.hist(df.loc[df.rotulo == c, "tempo_ms"], bins=bins, alpha=0.55, label=c, density=False)
plt.title("Distribuição dos RTTs")
plt.xlabel("tempo_ms")
plt.ylabel("Contagem")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


def qq_plot(serie, titulo):
    osm, osr = stats.probplot(serie, dist="norm")[:2]
    slope, intercept, r = stats.probplot(serie, dist="norm")[1]
    plt.figure(figsize=(6,5))
    plt.plot(osm[0], osm[1], 'o', ms=3)
    plt.plot(osm[0], slope*osm[0] + intercept, '-', lw=1)
    plt.title(titulo)
    plt.xlabel("Quantis teóricos")
    plt.ylabel("Quantis amostrais")
    plt.grid(alpha=0.3)
    plt.show()

for c in conexoes[:2]:  
    qq_plot(df.loc[df.rotulo == c, "tempo_ms"], f"QQ-Plot • {c}")


fig, ax = plt.subplots(figsize=(10,3))
ax.axis("off")
tbl = ax.table(cellText=resumo_df.values,
               rowLabels=resumo_df.index,
               colLabels=resumo_df.columns,
               loc="center", cellLoc="center")
tbl.auto_set_font_size(False)
tbl.set_fontsize(8)
tbl.scale(1.05, 1.2)
ax.set_title("Resumo estatístico (por conexão)")
plt.show()


fig, ax = plt.subplots(figsize=(10,3))
ax.axis("off")
ax.text(0.0, 0.95, "Testes estatísticos", fontsize=12, weight="bold", va="top")
ax.text(0.0, 0.80, testes_texto, fontsize=10, family="monospace", va="top")
ax.text(0.0, 0.10,
        "Interpretação rápida:\n"
        "• Shapiro: p>0.05 ⇒ não rejeita normalidade.\n"
        "• t-test: p<0.05 ⇒ diferença média significativa.",
        fontsize=9)
plt.show()
