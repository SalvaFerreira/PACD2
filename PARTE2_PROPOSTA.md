# Parte 2 do Projeto - Proposta de Dataset e Questões de Investigação
## Grupo 15 - Distrito de Setúbal

---

## 📋 Dataset Escolhido para a Parte 2

### Dataset Principal: Acidentes Rodoviários no Distrito de Setúbal
- **Fonte**: Dados fornecidos no projeto (acidentes-sample.xlsx)
- **Filtro**: Distrito de Setúbal
- **Período**: [A definir após análise dos dados]
- **Variáveis principais**: 
  - Temporais (data, hora, dia da semana)
  - Geográficas (concelho, tipo de via, coordenadas)
  - Gravidade (natureza do acidente, vítimas)
  - Condições (meteorologia, luminosidade, estado da via)
  - Demográficas (idade, género dos condutores)
  - Veículos (tipo de veículo envolvido)

### Dataset(s) Complementar(es) - Propostas:

#### Opção 1: Dados Demográficos e Socioeconómicos
- **Fonte**: INE (Instituto Nacional de Estatística) - [pordata.pt](https://www.pordata.pt/)
- **Dados a recolher**:
  - População por concelho
  - Densidade populacional
  - Taxa de desemprego
  - Rendimento médio por agregado familiar
  - Estrutura etária da população
  - Número de veículos registados por concelho
- **Objetivo**: Relacionar indicadores socioeconómicos com padrões de acidentes

#### Opção 2: Dados de Infraestrutura Viária
- **Fonte**: IMT (Instituto da Mobilidade e dos Transportes) / Infraestruturas de Portugal
- **Dados a recolher**:
  - Extensão da rede rodoviária por concelho
  - Tipos de vias (autoestradas, nacionais, municipais)
  - Estado de conservação das vias
  - Localizações de obras
  - Sinalização e iluminação
- **Objetivo**: Avaliar relação entre qualidade/tipo de infraestrutura e acidentes

#### Opção 3: Dados Meteorológicos Detalhados
- **Fonte**: IPMA (Instituto Português do Mar e da Atmosfera)
- **Dados a recolher**:
  - Precipitação diária por estação meteorológica
  - Temperatura
  - Velocidade do vento
  - Visibilidade
  - Condições de nebulosidade
- **Objetivo**: Análise mais profunda da influência das condições meteorológicas

#### Opção 4: Dados de Tráfego
- **Fonte**: Infraestruturas de Portugal / Câmaras Municipais
- **Dados a recolher**:
  - Tráfego médio diário (TMD) por troço
  - Velocidade média
  - Tipo de veículos circulantes
  - Pontos de congestionamento
- **Objetivo**: Relacionar volume de tráfego com taxa de acidentes

---

## 🔍 Questões de Investigação (Desafios)

### 1. Análise Temporal e Padrões

#### 1.1 Sazonalidade e Tendências
- **Questão**: Existem padrões sazonais significativos nos acidentes em Setúbal?
- **Sub-questões**:
  - Que meses apresentam maior incidência de acidentes?
  - Existe relação entre períodos de férias/festividades e aumento de acidentes?
  - Como evoluiu a taxa de acidentes ao longo dos anos?
  - Há diferenças significativas entre dias úteis e fins de semana?

#### 1.2 Períodos de Risco
- **Questão**: Quais são os períodos do dia com maior risco de acidentes graves?
- **Sub-questões**:
  - Existe diferença entre acidentes diurnos e noturnos em termos de gravidade?
  - As horas de ponta (rush) apresentam mais acidentes mas menos graves?
  - Como varia a gravidade dos acidentes ao longo do dia?

### 2. Análise Geográfica e Espacial

#### 2.1 Hotspots de Acidentes
- **Questão**: Quais são os pontos/troços mais perigosos do distrito de Setúbal?
- **Sub-questões**:
  - Que concelhos apresentam maior taxa de acidentes por habitante?
  - Que concelhos têm maior taxa de acidentes por km de estrada?
  - Existe clustering espacial de acidentes graves?
  - Que características têm os locais com mais acidentes?

#### 2.2 Infraestrutura e Acidentes
- **Questão**: Como o tipo e qualidade da via influenciam a ocorrência e gravidade dos acidentes?
- **Sub-questões**:
  - Autoestradas são mais seguras que estradas nacionais/municipais?
  - O estado de conservação da via tem impacto significativo?
  - Zonas urbanas vs. zonas rurais: onde há mais acidentes graves?

### 3. Fatores de Risco e Causalidade

#### 3.1 Condições Ambientais
- **Questão**: Que condições meteorológicas e de luminosidade estão mais associadas a acidentes graves?
- **Sub-questões**:
  - Quantos % dos acidentes graves ocorrem com chuva?
  - A falta de luminosidade aumenta a gravidade dos acidentes?
  - Existe correlação entre temperatura extrema e acidentes?
  - Nevoeiro é um fator de risco significativo em Setúbal?

#### 3.2 Perfil do Condutor
- **Questão**: Que características demográficas dos condutores estão associadas a maior risco?
- **Sub-questões**:
  - Que faixa etária apresenta maior taxa de acidentes?
  - Condutores jovens (<25 anos) têm acidentes mais graves?
  - Existe diferença significativa entre géneros?
  - Que perfil de condutor está mais envolvido em acidentes noturnos?

#### 3.3 Tipo de Veículo
- **Questão**: Que tipos de veículos estão mais envolvidos em acidentes e em que circunstâncias?
- **Sub-questões**:
  - Motociclos têm maior taxa de acidentes graves?
  - Veículos pesados estão mais envolvidos em que tipo de acidentes?
  - Que tipo de veículo está mais presente em acidentes com vítimas mortais?

### 4. Análise Preditiva e Modelação

#### 4.1 Previsão de Gravidade
- **Questão**: É possível prever a gravidade de um acidente com base nas circunstâncias?
- **Objetivo**: Desenvolver modelo de classificação (ML) para prever:
  - Acidentes com/sem vítimas
  - Gravidade (ligeiro, grave, mortal)
- **Features**: hora, local, condições meteorológicas, tipo de via, perfil condutor

#### 4.2 Identificação de Zonas de Alto Risco
- **Questão**: Que áreas têm maior probabilidade de acidentes graves no futuro?
- **Objetivo**: Criar modelo preditivo espacial
- **Aplicação**: Apoio à decisão para investimento em infraestrutura e fiscalização

#### 4.3 Séries Temporais
- **Questão**: Podemos prever a evolução do número de acidentes?
- **Objetivo**: Modelar tendências e fazer previsões para os próximos anos
- **Técnicas**: ARIMA, Prophet, ou modelos de ML para séries temporais

### 5. Análise Socioeconómica

#### 5.1 Indicadores Socioeconómicos e Acidentes
- **Questão**: Existe relação entre indicadores socioeconómicos e taxa de acidentes?
- **Sub-questões**:
  - Concelhos com maior densidade populacional têm mais acidentes per capita?
  - Taxa de desemprego influencia padrões de acidentes?
  - Rendimento médio está correlacionado com tipo/gravidade de acidentes?
  - Número de veículos registados explica diferenças entre concelhos?

#### 5.2 População e Risco
- **Questão**: Como a estrutura demográfica influencia os padrões de acidentes?
- **Sub-questões**:
  - Concelhos mais envelhecidos têm padrões diferentes?
  - Áreas com mais população jovem têm mais acidentes noturnos?

### 6. Impacto e Custos

#### 6.1 Custo Social dos Acidentes
- **Questão**: Qual é o impacto estimado dos acidentes em termos de vítimas e custos?
- **Análises**:
  - Total de vítimas (mortos, feridos graves, feridos ligeiros) por ano
  - Estimativa de custos diretos e indiretos
  - Concelhos/troços com maior "custo social"
  - Evolução temporal do impacto

#### 6.2 Eficácia de Medidas
- **Questão**: Houve redução de acidentes após implementação de medidas (se aplicável)?
- **Análises**:
  - Comparação antes/depois de obras de melhoramento
  - Impacto de campanhas de sensibilização
  - Efeito de alterações legislativas

---

## 🎯 Objetivos Específicos da Parte 2

1. **Integração de Dados**
   - Juntar dataset de acidentes com dados complementares escolhidos
   - Garantir consistência geográfica e temporal
   - Tratar valores em falta e outliers

2. **Análise Avançada**
   - Aplicar técnicas estatísticas (testes de hipóteses, correlações, regressões)
   - Desenvolver modelos de Machine Learning
   - Criar visualizações interativas avançadas

3. **Insights Acionáveis**
   - Identificar fatores de risco mais significativos
   - Propor recomendações baseadas em dados
   - Criar ferramentas de suporte à decisão

4. **Comunicação de Resultados**
   - Dashboard interativo
   - Relatório técnico detalhado
   - Apresentação executiva

---

## 📊 Metodologia Proposta

### Fase 1: Preparação (Semana 1)
- ✅ Análise exploratória dos dados de Setúbal
- ✅ Desenvolvimento de funções de processamento
- ⏳ Escolha definitiva do dataset complementar
- ⏳ Recolha e validação dos dados complementares

### Fase 2: Integração e Limpeza (Semana 2)
- Merge de datasets
- Tratamento de dados em falta
- Feature engineering
- Validação de consistência

### Fase 3: Análise Descritiva (Semana 3)
- Análise estatística detalhada
- Testes de hipóteses
- Visualizações avançadas
- Identificação de padrões

### Fase 4: Modelação (Semana 4)
- Desenvolvimento de modelos preditivos
- Validação e otimização
- Interpretação de resultados
- Análise de features importantes

### Fase 5: Comunicação (Semana 5)
- Criação de dashboard
- Redação de relatório
- Preparação de apresentação
- Documentação de código

---

## 🔧 Ferramentas e Técnicas

### Análise de Dados
- **Python**: Pandas, NumPy
- **Estatística**: SciPy, Statsmodels
- **Visualização**: Matplotlib, Seaborn, Plotly
- **Geoespacial**: Geopandas, Folium

### Machine Learning
- **Scikit-learn**: Modelos de classificação e regressão
- **XGBoost/LightGBM**: Modelos avançados de gradient boosting
- **Clustering**: K-means, DBSCAN para análise espacial

### Dashboard e Apresentação
- **Streamlit** ou **Dash**: Dashboard interativo
- **Jupyter Notebook**: Documentação e análise
- **PowerPoint/LaTeX**: Apresentação final

---

## 📝 Deliverables Esperados

1. **Código**
   - Scripts de processamento de dados
   - Notebooks de análise
   - Modelos treinados
   - Código do dashboard

2. **Documentação**
   - README detalhado
   - Dicionário de dados
   - Documentação de metodologia
   - Instruções de reprodução

3. **Visualizações**
   - Gráficos estáticos (alta qualidade para relatório)
   - Dashboard interativo
   - Mapas geográficos

4. **Relatório**
   - Introdução e contexto
   - Metodologia
   - Resultados e análises
   - Conclusões e recomendações
   - Referências

5. **Apresentação**
   - Slides executivos
   - Demonstração do dashboard
   - Principais insights e recomendações

---

## 📅 Cronograma Detalhado

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 1 | - Análise exploratória<br>- Escolha dataset complementar<br>- Recolha de dados | - Notebook EDA<br>- Dataset complementar |
| 2 | - Integração de dados<br>- Limpeza e preparação<br>- Feature engineering | - Dataset integrado<br>- Funções de processamento |
| 3 | - Análise estatística<br>- Visualizações avançadas<br>- Testes de hipóteses | - Análises detalhadas<br>- Gráficos |
| 4 | - Modelação ML<br>- Validação<br>- Interpretação | - Modelos treinados<br>- Métricas de performance |
| 5 | - Dashboard<br>- Relatório<br>- Apresentação | - Todos os deliverables finais |

---

## 🎓 Equipa e Responsabilidades

**Grupo 15 - Distrito de Setúbal**

### Distribuição de Tarefas (Sugerida):
1. **Recolha e Integração de Dados**: [Nome(s)]
2. **Análise Estatística e Visualizações**: [Nome(s)]
3. **Modelação e Machine Learning**: [Nome(s)]
4. **Dashboard e Interface**: [Nome(s)]
5. **Relatório e Documentação**: [Nome(s)]

*Nota: Todos os membros devem estar envolvidos em múltiplas áreas e revisão cruzada.*

---

## 📚 Referências Iniciais

1. **ANSR** - Autoridade Nacional de Segurança Rodoviária
   - Relatórios anuais de sinistralidade
   - Estatísticas nacionais e regionais

2. **INE** - Instituto Nacional de Estatística
   - Dados demográficos e socioeconómicos
   - PORDATA para séries temporais

3. **IMT** - Instituto da Mobilidade e dos Transportes
   - Dados de infraestrutura
   - Regulamentação rodoviária

4. **Artigos Científicos**:
   - Análise de fatores de risco em acidentes rodoviários
   - Modelos preditivos de acidentes
   - Análise espacial de sinistralidade

---

## 🔄 Próximas Ações Imediatas

- [ ] Reunião de equipa para decidir dataset complementar definitivo
- [ ] Identificar fontes exatas e forma de acesso aos dados
- [ ] Distribuir responsabilidades específicas
- [ ] Criar repositório GitHub para colaboração
- [ ] Iniciar recolha de dados complementares
- [ ] Agendar reuniões de acompanhamento semanal

---

*Documento em desenvolvimento - Grupo 15*  
*Última atualização: [Data]*
