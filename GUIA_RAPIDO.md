# Guia de Início Rápido - Projeto PACD2
## Grupo 15 - Distrito de Setúbal

---

## ⚡ Passos Rápidos para Começar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar a Análise Exploratória

Abrir o Jupyter Notebook:
```bash
jupyter notebook analise_setubal.ipynb
```

Ou executar células diretamente no VS Code (recomendado).

### 3. Usar os Módulos Python

```python
# Importar módulos
from src.data_processing import AcidentesSetubal
from src.visualizacoes import VisualizadorAcidentes

# Processar dados
processador = AcidentesSetubal('dados/acidentes-sample.xlsx')
processador.carregar_dados()
processador.filtrar_setubal()
processador.preparar_datas()

# Ver estatísticas
stats = processador.obter_estatisticas_basicas()
print(stats)

# Criar visualizações
viz = VisualizadorAcidentes(processador.df_setubal)
viz.grafico_temporal('ANO')
viz.grafico_top_categorias('CONC_ACIDENTE', top_n=5)
```

---

## 📁 Ficheiros Importantes

| Ficheiro | Descrição |
|----------|-----------|
| `analise_setubal.ipynb` | Notebook principal com toda a análise |
| `src/data_processing.py` | Funções para processar dados |
| `src/visualizacoes.py` | Funções para criar gráficos |
| `PARTE2_PROPOSTA.md` | Proposta detalhada para Parte 2 |
| `requirements.txt` | Lista de dependências |

---

## 🎯 Objetivos da Semana

- [x] ✅ Começar análise exploratória dos dados
- [x] ✅ Terminar desenvolvimento da parte 1 do projeto
- [x] ✅ Escolher conjunto de dados para parte 2
- [x] ✅ Pensar em questões (desafios) para resolver

---

## 📊 O Que Já Foi Feito

### Parte 1 - Análise Exploratória
1. **Notebook Completo**: `analise_setubal.ipynb`
   - Estrutura completa de análise
   - Visualizações temporais, geográficas, demográficas
   - Análise de condições e gravidade
   - Correlações e análises cruzadas

2. **Módulos Python Criados**:
   - `data_processing.py`: Classe `AcidentesSetubal`
     - Carregar e filtrar dados
     - Preparar datas e features
     - Calcular estatísticas
     - Filtros avançados
   
   - `visualizacoes.py`: Classe `VisualizadorAcidentes`
     - Gráficos temporais
     - Top categorias
     - Mapas interativos
     - Dashboard completo

3. **Documentação**:
   - README.md atualizado
   - PARTE2_PROPOSTA.md com questões de investigação
   - Este guia de início rápido

---

## 🔍 Próximas Ações

### Para Esta Semana
1. **Executar a Análise**
   - Abrir `analise_setubal.ipynb`
   - Executar todas as células
   - Revisar resultados e visualizações

2. **Finalizar Parte 1**
   - Adicionar observações específicas aos padrões encontrados
   - Completar seções de conclusões no notebook
   - Exportar gráficos importantes

3. **Preparar Parte 2**
   - Ler `PARTE2_PROPOSTA.md`
   - Escolher dataset complementar definitivo
   - Começar a recolher dados adicionais

### Reunião de Equipa (Sugerido)
- Discutir resultados da análise exploratória
- Decidir dataset complementar
- Distribuir tarefas da Parte 2
- Definir questões de investigação prioritárias

---

## 💡 Dicas Úteis

### Executar Análise Rápida
Se quiser apenas ver resultados rápidos sem o notebook:

```python
# No terminal Python ou script
from src.data_processing import AcidentesSetubal

processador = AcidentesSetubal('dados/acidentes-sample.xlsx')
processador.carregar_dados()
processador.filtrar_setubal()
processador.preparar_datas()

# Ver resumo
print("\n📊 RESUMO:")
print(f"Total acidentes: {len(processador.df_setubal)}")
print(f"Período: {processador.df_setubal['ANO'].min()} - {processador.df_setubal['ANO'].max()}")
print(f"\nTop 5 Concelhos:")
print(processador.acidentes_por_concelho(top_n=5))
```

### Exportar Dados Tratados
```python
processador.exportar_dados_tratados(formato='csv')
processador.exportar_dados_tratados(formato='excel')
```

### Criar Dashboard de Visualizações
```python
from src.visualizacoes import VisualizadorAcidentes

viz = VisualizadorAcidentes(processador.df_setubal)
viz.dashboard_resumo(salvar_pasta='dados/graficos')
```

---

## ❓ Troubleshooting

### Problema: Módulos não encontrados
```bash
# Certifique-se que está no diretório correto
cd PACD2

# Reinstalar dependências
pip install -r requirements.txt
```

### Problema: Jupyter não abre
```bash
# Instalar Jupyter
pip install jupyter notebook

# Ou usar VS Code com extensão Python
```

### Problema: Dados não carregam
- Verificar se `dados/acidentes-sample.xlsx` existe
- Verificar caminho do ficheiro no código

---

## 📞 Ajuda

Para questões sobre:
- **Código**: Ver comentários em `data_processing.py` e `visualizacoes.py`
- **Análise**: Ver seções do notebook `analise_setubal.ipynb`
- **Parte 2**: Ver `PARTE2_PROPOSTA.md`

---

## ✅ Checklist de Progresso

### Parte 1
- [x] Análise exploratória iniciada
- [x] Funções de processamento criadas
- [x] Módulo de visualizações criado
- [ ] Notebook executado com dados reais
- [ ] Observações e conclusões adicionadas
- [ ] Gráficos exportados

### Parte 2
- [x] Proposta documentada
- [x] Questões de investigação definidas
- [ ] Dataset complementar escolhido
- [ ] Dados complementares recolhidos
- [ ] Integração de dados iniciada

---

*Última atualização: Novembro 2025*
