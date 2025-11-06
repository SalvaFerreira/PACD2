# Projeto PACD2 - Análise de Acidentes Rodoviários
## Grupo 15 - Distrito de Setúbal

---

## 📋 Sobre o Projeto

Este projeto tem como objetivo analisar dados de acidentes rodoviários no distrito de Setúbal, identificar padrões e fatores de risco, e desenvolver modelos preditivos para apoiar a tomada de decisões na área da segurança rodoviária.

### Parte 1: Análise Exploratória de Dados
- Exploração e visualização de dados de acidentes em Setúbal
- Identificação de padrões temporais, geográficos e demográficos
- Análise de condições associadas aos acidentes

### Parte 2: Análise Avançada e Modelação
- Integração com datasets complementares
- Desenvolvimento de modelos preditivos
- Criação de dashboard interativo
- Recomendações baseadas em dados

---

## 📂 Estrutura do Projeto

```
PACD2/
├── README.md                    # Este ficheiro
├── PARTE2_PROPOSTA.md          # Proposta detalhada para Parte 2
├── requirements.txt             # Dependências Python
├── analise_setubal.ipynb       # Notebook principal de análise
├── dados/                       # Pasta de dados
│   ├── acidentes-sample.xlsx   # Dados originais
│   ├── acidentes_setubal_tratado.csv
│   ├── acidentes_setubal_tratado.xlsx
│   └── graficos/               # Gráficos exportados
├── src/                         # Código fonte
│   ├── data_processing.py      # Funções de processamento
│   └── visualizacoes.py        # Funções de visualização
└── documentos/                  # Documentação adicional
```

---

## 🚀 Como Começar

### 1. Clonar o Repositório
```bash
git clone [URL_DO_REPOSITORIO]
cd PACD2
```

### 2. Criar Ambiente Virtual (Recomendado)
```bash
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Abrir o Notebook
```bash
jupyter notebook analise_setubal.ipynb
```

---

## 📊 Análises Realizadas

### Análise Temporal
- Distribuição de acidentes por ano, mês, dia da semana e hora
- Identificação de períodos de maior risco
- Análise de sazonalidade

### Análise Geográfica
- Distribuição por concelho
- Identificação de hotspots
- Análise por tipo de via

### Análise de Gravidade
- Tipos de acidentes (natureza)
- Análise de vítimas
- Fatores associados à gravidade

### Análise de Condições
- Condições meteorológicas
- Luminosidade
- Estado da via

### Análise Demográfica
- Perfil dos condutores (idade, género)
- Tipos de veículos envolvidos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib** - Visualizações estáticas
- **Seaborn** - Visualizações estatísticas
- **Plotly** - Visualizações interativas
- **Jupyter** - Notebooks interativos
- **Scikit-learn** - Machine Learning (Parte 2)

---

## 📈 Principais Resultados (Parte 1)

*[A preencher após executar a análise]*

### Destaques:
- Total de acidentes analisados em Setúbal: [X]
- Período de análise: [YYYY - YYYY]
- Concelho com mais acidentes: [Nome]
- Mês com mais acidentes: [Mês]
- Hora de maior risco: [XX]h

---

## 🎯 Próximos Passos (Parte 2)

1. ✅ Análise exploratória concluída
2. ⏳ Escolha do dataset complementar
3. ⏳ Integração de dados
4. ⏳ Modelação preditiva
5. ⏳ Dashboard interativo
6. ⏳ Relatório final

Ver [PARTE2_PROPOSTA.md](PARTE2_PROPOSTA.md) para detalhes completos.

---

## 👥 Equipa

**Grupo 15 - Distrito de Setúbal**

- [Nome 1] - [Responsabilidades]
- [Nome 2] - [Responsabilidades]
- [Nome 3] - [Responsabilidades]
- [...]

---

## 📝 Como Usar os Módulos

### Processamento de Dados

```python
from src.data_processing import AcidentesSetubal

# Inicializar processador
processador = AcidentesSetubal('dados/acidentes-sample.xlsx')

# Carregar e filtrar dados
processador.carregar_dados()
processador.filtrar_setubal()
processador.preparar_datas()

# Obter estatísticas
stats = processador.obter_estatisticas_basicas()
print(stats)

# Acidentes por ano
acidentes_ano = processador.acidentes_por_periodo('ANO')
print(acidentes_ano)

# Top 5 concelhos
top_concelhos = processador.acidentes_por_concelho(top_n=5)
print(top_concelhos)
```

### Visualizações

```python
from src.visualizacoes import VisualizadorAcidentes

# Criar visualizador
viz = VisualizadorAcidentes(processador.df_setubal)

# Gráfico temporal
viz.grafico_temporal('ANO', titulo='Acidentes por Ano - Setúbal')

# Top concelhos
viz.grafico_top_categorias('CONC_ACIDENTE', top_n=10)

# Dashboard completo
viz.dashboard_resumo(salvar_pasta='dados/graficos')
```

---

## 📚 Referências

1. **ANSR** - Autoridade Nacional de Segurança Rodoviária
2. **INE** - Instituto Nacional de Estatística
3. **PORDATA** - Base de dados Portugal Contemporâneo
4. **IMT** - Instituto da Mobilidade e dos Transportes

---

## 📄 Licença

[Ver LICENSE](LICENSE)

---

## 📧 Contacto

Para questões sobre o projeto, contactar:
- [Email do grupo/responsável]

---

*Última atualização: Novembro 2025*
