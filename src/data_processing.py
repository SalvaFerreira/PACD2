"""
Módulo para processamento de dados de acidentes rodoviários
Distrito de Setúbal - Grupo 15
"""

import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Tuple
from datetime import datetime


class AcidentesSetubal:
    """
    Classe para carregar e processar dados de acidentes no distrito de Setúbal
    """
    
    def __init__(self, filepath: str):
        """
        Inicializa o processador de dados
        
        Args:
            filepath: Caminho para o ficheiro Excel com dados de acidentes
        """
        self.filepath = filepath
        self.df_completo = None
        self.df_setubal = None
        
    def carregar_dados(self) -> pd.DataFrame:
        """
        Carrega os dados do ficheiro Excel
        
        Returns:
            DataFrame com todos os acidentes
        """
        print(f"📂 A carregar dados de: {self.filepath}")
        self.df_completo = pd.read_excel(self.filepath)
        print(f"✓ Carregados {len(self.df_completo)} registos")
        return self.df_completo
    
    def filtrar_setubal(self, coluna_distrito: str = 'DIST_ACIDENTE') -> pd.DataFrame:
        """
        Filtra apenas os acidentes do distrito de Setúbal
        
        Args:
            coluna_distrito: Nome da coluna que contém o distrito
            
        Returns:
            DataFrame filtrado para Setúbal
        """
        if self.df_completo is None:
            self.carregar_dados()
        
        # Filtrar Setúbal (pode estar escrito de diferentes formas)
        self.df_setubal = self.df_completo[
            self.df_completo[coluna_distrito].str.upper().str.contains('SET[UÚ]BAL', na=False)
        ].copy()
        
        print(f"✓ Filtrados {len(self.df_setubal)} acidentes em Setúbal")
        print(f"  ({len(self.df_setubal)/len(self.df_completo)*100:.2f}% do total)")
        
        return self.df_setubal
    
    def preparar_datas(self, coluna_data: str = 'DATA_ACIDENTE') -> None:
        """
        Processa a coluna de data e cria colunas derivadas
        
        Args:
            coluna_data: Nome da coluna com a data do acidente
        """
        if self.df_setubal is None:
            raise ValueError("Deve primeiro filtrar os dados de Setúbal")
        
        # Converter para datetime
        self.df_setubal[coluna_data] = pd.to_datetime(self.df_setubal[coluna_data])
        
        # Criar colunas derivadas
        self.df_setubal['ANO'] = self.df_setubal[coluna_data].dt.year
        self.df_setubal['MES'] = self.df_setubal[coluna_data].dt.month
        self.df_setubal['DIA'] = self.df_setubal[coluna_data].dt.day
        self.df_setubal['DIA_SEMANA'] = self.df_setubal[coluna_data].dt.day_name()
        self.df_setubal['DIA_SEMANA_NUM'] = self.df_setubal[coluna_data].dt.dayofweek
        self.df_setubal['HORA'] = self.df_setubal[coluna_data].dt.hour
        self.df_setubal['TRIMESTRE'] = self.df_setubal[coluna_data].dt.quarter
        self.df_setubal['FIM_DE_SEMANA'] = self.df_setubal['DIA_SEMANA_NUM'].isin([5, 6])
        
        print("✓ Colunas temporais criadas: ANO, MES, DIA, DIA_SEMANA, HORA, TRIMESTRE, FIM_DE_SEMANA")
    
    def obter_estatisticas_basicas(self) -> Dict:
        """
        Calcula estatísticas básicas sobre os acidentes
        
        Returns:
            Dicionário com estatísticas
        """
        if self.df_setubal is None:
            raise ValueError("Deve primeiro filtrar os dados de Setúbal")
        
        stats = {
            'total_acidentes': len(self.df_setubal),
            'periodo': f"{self.df_setubal['ANO'].min()} - {self.df_setubal['ANO'].max()}" if 'ANO' in self.df_setubal.columns else 'N/A',
            'concelhos': self.df_setubal['CONC_ACIDENTE'].nunique() if 'CONC_ACIDENTE' in self.df_setubal.columns else 0,
            'valores_faltantes': self.df_setubal.isnull().sum().sum(),
            'percentagem_completos': (1 - self.df_setubal.isnull().sum().sum() / (len(self.df_setubal) * len(self.df_setubal.columns))) * 100
        }
        
        return stats
    
    def acidentes_por_periodo(self, periodo: str = 'ANO') -> pd.Series:
        """
        Agrupa acidentes por período temporal
        
        Args:
            periodo: 'ANO', 'MES', 'DIA_SEMANA', 'HORA', etc.
            
        Returns:
            Series com contagem de acidentes por período
        """
        if periodo not in self.df_setubal.columns:
            raise ValueError(f"Coluna {periodo} não existe. Execute preparar_datas() primeiro.")
        
        return self.df_setubal[periodo].value_counts().sort_index()
    
    def acidentes_por_concelho(self, top_n: Optional[int] = None) -> pd.Series:
        """
        Agrupa acidentes por concelho
        
        Args:
            top_n: Se especificado, retorna apenas os top N concelhos
            
        Returns:
            Series com contagem de acidentes por concelho
        """
        resultado = self.df_setubal['CONC_ACIDENTE'].value_counts()
        
        if top_n:
            resultado = resultado.head(top_n)
        
        return resultado
    
    def filtrar_por_condicoes(self, 
                             ano: Optional[int] = None,
                             concelho: Optional[str] = None,
                             natureza: Optional[str] = None,
                             periodo_hora: Optional[Tuple[int, int]] = None) -> pd.DataFrame:
        """
        Filtra acidentes por múltiplas condições
        
        Args:
            ano: Ano específico
            concelho: Nome do concelho
            natureza: Natureza do acidente
            periodo_hora: Tuplo (hora_inicio, hora_fim)
            
        Returns:
            DataFrame filtrado
        """
        df_filtrado = self.df_setubal.copy()
        
        if ano and 'ANO' in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado['ANO'] == ano]
        
        if concelho and 'CONC_ACIDENTE' in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado['CONC_ACIDENTE'].str.upper() == concelho.upper()]
        
        if natureza and 'NATUREZA_ACIDENTE' in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado['NATUREZA_ACIDENTE'].str.upper() == natureza.upper()]
        
        if periodo_hora and 'HORA' in df_filtrado.columns:
            hora_inicio, hora_fim = periodo_hora
            df_filtrado = df_filtrado[
                (df_filtrado['HORA'] >= hora_inicio) & 
                (df_filtrado['HORA'] <= hora_fim)
            ]
        
        return df_filtrado
    
    def analisar_gravidade(self) -> Dict:
        """
        Analisa a gravidade dos acidentes
        
        Returns:
            Dicionário com estatísticas de gravidade
        """
        stats = {}
        
        if 'NATUREZA_ACIDENTE' in self.df_setubal.columns:
            stats['por_natureza'] = self.df_setubal['NATUREZA_ACIDENTE'].value_counts().to_dict()
        
        # Procurar colunas relacionadas com vítimas
        colunas_vitimas = [col for col in self.df_setubal.columns 
                          if any(palavra in col.upper() for palavra in ['VITIMA', 'FERIDO', 'MORTO'])]
        
        for col in colunas_vitimas:
            if pd.api.types.is_numeric_dtype(self.df_setubal[col]):
                stats[col] = {
                    'total': self.df_setubal[col].sum(),
                    'media': self.df_setubal[col].mean(),
                    'maximo': self.df_setubal[col].max()
                }
        
        return stats
    
    def exportar_dados_tratados(self, 
                               formato: str = 'csv',
                               caminho: str = 'dados/acidentes_setubal_tratado') -> None:
        """
        Exporta dados tratados
        
        Args:
            formato: 'csv' ou 'excel'
            caminho: Caminho base para o ficheiro (sem extensão)
        """
        if self.df_setubal is None:
            raise ValueError("Deve primeiro filtrar os dados de Setúbal")
        
        if formato.lower() == 'csv':
            self.df_setubal.to_csv(f"{caminho}.csv", index=False, encoding='utf-8')
            print(f"✓ Dados exportados para: {caminho}.csv")
        elif formato.lower() in ['excel', 'xlsx']:
            self.df_setubal.to_excel(f"{caminho}.xlsx", index=False)
            print(f"✓ Dados exportados para: {caminho}.xlsx")
        else:
            raise ValueError(f"Formato '{formato}' não suportado. Use 'csv' ou 'excel'")


def exemplo_uso():
    """
    Exemplo de como usar a classe AcidentesSetubal
    """
    # Inicializar
    processador = AcidentesSetubal('dados/acidentes-sample.xlsx')
    
    # Carregar e filtrar
    processador.carregar_dados()
    processador.filtrar_setubal()
    processador.preparar_datas()
    
    # Obter estatísticas
    stats = processador.obter_estatisticas_basicas()
    print("\n📊 Estatísticas Básicas:")
    for chave, valor in stats.items():
        print(f"  {chave}: {valor}")
    
    # Acidentes por ano
    print("\n📅 Acidentes por ano:")
    print(processador.acidentes_por_periodo('ANO'))
    
    # Top 5 concelhos
    print("\n🏘️ Top 5 concelhos:")
    print(processador.acidentes_por_concelho(top_n=5))
    
    # Exportar
    processador.exportar_dados_tratados()


if __name__ == "__main__":
    exemplo_uso()
