"""
Módulo de visualizações para análise de acidentes rodoviários
Distrito de Setúbal - Grupo 15
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from typing import Optional, List, Tuple
from pathlib import Path


class VisualizadorAcidentes:
    """
    Classe para criar visualizações dos dados de acidentes
    """
    
    def __init__(self, df: pd.DataFrame, estilo: str = 'seaborn-v0_8-darkgrid'):
        """
        Inicializa o visualizador
        
        Args:
            df: DataFrame com dados de acidentes
            estilo: Estilo do matplotlib
        """
        self.df = df
        plt.style.use(estilo)
        sns.set_palette("husl")
        
    def grafico_temporal(self, 
                        periodo: str = 'ANO',
                        titulo: Optional[str] = None,
                        cor: str = 'steelblue',
                        figsize: Tuple[int, int] = (12, 6),
                        salvar: Optional[str] = None) -> None:
        """
        Cria gráfico de barras para distribuição temporal
        
        Args:
            periodo: Coluna temporal ('ANO', 'MES', 'DIA_SEMANA', etc.)
            titulo: Título do gráfico
            cor: Cor das barras
            figsize: Tamanho da figura
            salvar: Caminho para salvar o gráfico
        """
        dados = self.df[periodo].value_counts().sort_index()
        
        fig, ax = plt.subplots(figsize=figsize)
        dados.plot(kind='bar', ax=ax, color=cor)
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'Distribuição de Acidentes por {periodo}', fontsize=14, fontweight='bold')
        
        ax.set_xlabel(periodo, fontsize=12)
        ax.set_ylabel('Número de Acidentes', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def grafico_linha_temporal(self,
                              coluna: str = 'HORA',
                              titulo: Optional[str] = None,
                              cor: str = 'darkred',
                              figsize: Tuple[int, int] = (14, 6),
                              salvar: Optional[str] = None) -> None:
        """
        Cria gráfico de linha para padrões temporais
        
        Args:
            coluna: Coluna temporal
            titulo: Título do gráfico
            cor: Cor da linha
            figsize: Tamanho da figura
            salvar: Caminho para salvar
        """
        dados = self.df[coluna].value_counts().sort_index()
        
        fig, ax = plt.subplots(figsize=figsize)
        dados.plot(kind='line', marker='o', ax=ax, color=cor, linewidth=2)
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'Padrão de Acidentes por {coluna}', fontsize=14, fontweight='bold')
        
        ax.set_xlabel(coluna, fontsize=12)
        ax.set_ylabel('Número de Acidentes', fontsize=12)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def grafico_top_categorias(self,
                              coluna: str,
                              top_n: int = 10,
                              horizontal: bool = True,
                              titulo: Optional[str] = None,
                              cor: str = 'teal',
                              figsize: Tuple[int, int] = (12, 8),
                              salvar: Optional[str] = None) -> None:
        """
        Cria gráfico de barras para top categorias
        
        Args:
            coluna: Coluna a visualizar
            top_n: Número de categorias a mostrar
            horizontal: Se True, barras horizontais
            titulo: Título do gráfico
            cor: Cor das barras
            figsize: Tamanho da figura
            salvar: Caminho para salvar
        """
        dados = self.df[coluna].value_counts().head(top_n)
        
        fig, ax = plt.subplots(figsize=figsize)
        
        if horizontal:
            dados.plot(kind='barh', ax=ax, color=cor)
            ax.set_xlabel('Número de Acidentes', fontsize=12)
            ax.set_ylabel(coluna, fontsize=12)
            ax.grid(axis='x', alpha=0.3)
        else:
            dados.plot(kind='bar', ax=ax, color=cor)
            ax.set_xlabel(coluna, fontsize=12)
            ax.set_ylabel('Número de Acidentes', fontsize=12)
            ax.grid(axis='y', alpha=0.3)
            plt.xticks(rotation=45, ha='right')
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'Top {top_n} - {coluna}', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def grafico_pizza(self,
                     coluna: str,
                     titulo: Optional[str] = None,
                     figsize: Tuple[int, int] = (10, 6),
                     cores: Optional[List[str]] = None,
                     salvar: Optional[str] = None) -> None:
        """
        Cria gráfico de pizza
        
        Args:
            coluna: Coluna a visualizar
            titulo: Título do gráfico
            figsize: Tamanho da figura
            cores: Lista de cores
            salvar: Caminho para salvar
        """
        dados = self.df[coluna].value_counts()
        
        fig, ax = plt.subplots(figsize=figsize)
        dados.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90, colors=cores)
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'Distribuição - {coluna}', fontsize=14, fontweight='bold')
        
        ax.set_ylabel('')
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def histograma(self,
                  coluna: str,
                  bins: int = 30,
                  titulo: Optional[str] = None,
                  cor: str = 'green',
                  figsize: Tuple[int, int] = (12, 6),
                  salvar: Optional[str] = None) -> None:
        """
        Cria histograma para variável numérica
        
        Args:
            coluna: Coluna numérica
            bins: Número de bins
            titulo: Título do gráfico
            cor: Cor do histograma
            figsize: Tamanho da figura
            salvar: Caminho para salvar
        """
        fig, ax = plt.subplots(figsize=figsize)
        self.df[coluna].hist(bins=bins, ax=ax, color=cor, alpha=0.7, edgecolor='black')
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'Distribuição - {coluna}', fontsize=14, fontweight='bold')
        
        ax.set_xlabel(coluna, fontsize=12)
        ax.set_ylabel('Frequência', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def matriz_correlacao(self,
                         titulo: str = 'Matriz de Correlação',
                         figsize: Tuple[int, int] = (14, 10),
                         salvar: Optional[str] = None) -> None:
        """
        Cria heatmap de correlação para variáveis numéricas
        
        Args:
            titulo: Título do gráfico
            figsize: Tamanho da figura
            salvar: Caminho para salvar
        """
        # Selecionar apenas colunas numéricas
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            print("⚠️ Não há colunas numéricas suficientes para matriz de correlação")
            return
        
        correlation_matrix = self.df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=ax, square=True)
        ax.set_title(titulo, fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def grafico_cruzado(self,
                       coluna_x: str,
                       coluna_y: str,
                       stacked: bool = True,
                       titulo: Optional[str] = None,
                       figsize: Tuple[int, int] = (14, 6),
                       salvar: Optional[str] = None) -> None:
        """
        Cria gráfico cruzado entre duas variáveis categóricas
        
        Args:
            coluna_x: Primeira variável
            coluna_y: Segunda variável
            stacked: Se True, barras empilhadas
            titulo: Título do gráfico
            figsize: Tamanho da figura
            salvar: Caminho para salvar
        """
        crosstab = pd.crosstab(self.df[coluna_x], self.df[coluna_y])
        
        fig, ax = plt.subplots(figsize=figsize)
        crosstab.plot(kind='bar', stacked=stacked, ax=ax)
        
        if titulo:
            ax.set_title(titulo, fontsize=14, fontweight='bold')
        else:
            ax.set_title(f'{coluna_x} vs {coluna_y}', fontsize=14, fontweight='bold')
        
        ax.set_xlabel(coluna_x, fontsize=12)
        ax.set_ylabel('Número de Acidentes', fontsize=12)
        ax.legend(title=coluna_y, bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def mapa_interativo(self,
                       lat_col: str = 'LATITUDE',
                       lon_col: str = 'LONGITUDE',
                       hover_data: Optional[List[str]] = None,
                       titulo: str = 'Mapa de Acidentes - Setúbal',
                       salvar: Optional[str] = None) -> None:
        """
        Cria mapa interativo com plotly
        
        Args:
            lat_col: Coluna com latitude
            lon_col: Coluna com longitude
            hover_data: Colunas adicionais para mostrar ao passar o rato
            titulo: Título do mapa
            salvar: Caminho para salvar (HTML)
        """
        if lat_col not in self.df.columns or lon_col not in self.df.columns:
            print(f"⚠️ Colunas {lat_col} e/ou {lon_col} não encontradas")
            return
        
        # Remover linhas sem coordenadas
        df_map = self.df.dropna(subset=[lat_col, lon_col])
        
        if len(df_map) == 0:
            print("⚠️ Não há coordenadas válidas para plotar")
            return
        
        fig = px.scatter_mapbox(
            df_map,
            lat=lat_col,
            lon=lon_col,
            hover_data=hover_data,
            zoom=9,
            height=600,
            title=titulo
        )
        
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
        
        if salvar:
            fig.write_html(salvar)
            print(f"✓ Mapa salvo em: {salvar}")
        
        fig.show()
    
    def dashboard_resumo(self,
                        salvar_pasta: Optional[str] = None) -> None:
        """
        Cria dashboard com múltiplos gráficos
        
        Args:
            salvar_pasta: Pasta onde salvar os gráficos
        """
        if salvar_pasta:
            Path(salvar_pasta).mkdir(parents=True, exist_ok=True)
        
        # 1. Temporal
        if 'ANO' in self.df.columns:
            caminho = f"{salvar_pasta}/acidentes_por_ano.png" if salvar_pasta else None
            self.grafico_temporal('ANO', 'Acidentes por Ano - Setúbal', salvar=caminho)
        
        # 2. Mês
        if 'MES' in self.df.columns:
            caminho = f"{salvar_pasta}/acidentes_por_mes.png" if salvar_pasta else None
            self.grafico_temporal('MES', 'Acidentes por Mês - Setúbal', cor='coral', salvar=caminho)
        
        # 3. Hora
        if 'HORA' in self.df.columns:
            caminho = f"{salvar_pasta}/acidentes_por_hora.png" if salvar_pasta else None
            self.grafico_linha_temporal('HORA', 'Acidentes por Hora do Dia - Setúbal', salvar=caminho)
        
        # 4. Concelhos
        if 'CONC_ACIDENTE' in self.df.columns:
            caminho = f"{salvar_pasta}/top_concelhos.png" if salvar_pasta else None
            self.grafico_top_categorias('CONC_ACIDENTE', titulo='Top 10 Concelhos - Setúbal', salvar=caminho)
        
        # 5. Natureza
        if 'NATUREZA_ACIDENTE' in self.df.columns:
            caminho = f"{salvar_pasta}/natureza_acidente.png" if salvar_pasta else None
            self.grafico_top_categorias('NATUREZA_ACIDENTE', horizontal=False, 
                                       titulo='Natureza dos Acidentes - Setúbal', 
                                       cor='darkred', salvar=caminho)
        
        print("✓ Dashboard criado com sucesso!")


def exemplo_uso():
    """
    Exemplo de uso do visualizador
    """
    # Carregar dados (exemplo)
    from data_processing import AcidentesSetubal
    
    processador = AcidentesSetubal('dados/acidentes-sample.xlsx')
    processador.carregar_dados()
    processador.filtrar_setubal()
    processador.preparar_datas()
    
    # Criar visualizador
    viz = VisualizadorAcidentes(processador.df_setubal)
    
    # Criar gráficos
    viz.grafico_temporal('ANO')
    viz.grafico_top_categorias('CONC_ACIDENTE', top_n=5)
    
    # Criar dashboard completo
    viz.dashboard_resumo(salvar_pasta='dados/graficos')


if __name__ == "__main__":
    exemplo_uso()
