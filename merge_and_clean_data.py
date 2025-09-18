import pandas as pd
import numpy as np
import os

def load_and_examine_data():
    """Load all CSV files and examine their structure"""
    print("Loading CSV files...")
    
    # Load the data
    acidentes = pd.read_csv('acidentes_2023.csv')
    condutores = pd.read_csv('condutores_2023.csv')
    passageiros = pd.read_csv('passageiros_2023.csv')
    peoes = pd.read_csv('peões_2023.csv')
    
    print(f"Acidentes: {acidentes.shape[0]} rows, {acidentes.shape[1]} columns")
    print(f"Condutores: {condutores.shape[0]} rows, {condutores.shape[1]} columns")
    print(f"Passageiros: {passageiros.shape[0]} rows, {passageiros.shape[1]} columns")
    print(f"Peões: {peoes.shape[0]} rows, {peoes.shape[1]} columns")
    
    return acidentes, condutores, passageiros, peoes

def clean_and_merge_data(acidentes, condutores, passageiros, peoes):
    """Clean and merge all datasets"""
    print("\nCleaning and merging data...")
    
    # Start with accidents as the base table
    merged_data = acidentes.copy()
    
    # Merge with drivers (condutores) - left join to keep all accidents
    merged_data = merged_data.merge(condutores, on='Id. Acidente', how='left', suffixes=('', '_condutor'))
    print(f"After merging with condutores: {merged_data.shape}")
    
    # Merge with passengers (passageiros) - left join
    merged_data = merged_data.merge(passageiros, on=['Id. Acidente', 'Id. Veículo'], how='left', suffixes=('', '_passageiro'))
    print(f"After merging with passageiros: {merged_data.shape}")
    
    # Merge with pedestrians (peões) - left join
    merged_data = merged_data.merge(peoes, on='Id. Acidente', how='left', suffixes=('', '_peao'))
    print(f"After merging with peões: {merged_data.shape}")
    
    return merged_data

def create_motorcycle_subsets(merged_data):
    """Create subsets for motorcycles based on engine capacity"""
    print("\nCreating motorcycle subsets...")
    
    # Find motorcycle-related records
    print("Available vehicle categories:")
    if 'Categoria Veículos' in merged_data.columns:
        print(merged_data['Categoria Veículos'].value_counts())
    
    # Filter for motorcycles <= 125cc
    motorcycles_125cc_or_less = merged_data[
        merged_data['Categoria Veículos'].str.contains('Motociclo cilindrada <= 125cc', na=False)
    ].copy()
    
    # Filter for motorcycles > 125cc
    motorcycles_over_125cc = merged_data[
        merged_data['Categoria Veículos'].str.contains('Motociclo cilindrada > 125cc', na=False)
    ].copy()
    
    print(f"Motorcycles <= 125cc: {motorcycles_125cc_or_less.shape[0]} records")
    print(f"Motorcycles > 125cc: {motorcycles_over_125cc.shape[0]} records")
    
    return motorcycles_125cc_or_less, motorcycles_over_125cc

def clean_data(df):
    """Clean the dataset by handling missing values and data types"""
    print(f"\nCleaning dataset with {df.shape[0]} rows and {df.shape[1]} columns...")
    
    # Display missing values summary
    missing_summary = df.isnull().sum()
    missing_percent = (missing_summary / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing_summary,
        'Missing Percentage': missing_percent
    })
    missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Percentage', ascending=False)
    
    if not missing_df.empty:
        print(f"Columns with missing values (top 10):")
        print(missing_df.head(10))
    
    # Remove completely empty columns
    df_cleaned = df.dropna(axis=1, how='all')
    
    # Handle duplicate rows
    initial_rows = df_cleaned.shape[0]
    df_cleaned = df_cleaned.drop_duplicates()
    final_rows = df_cleaned.shape[0]
    
    if initial_rows != final_rows:
        print(f"Removed {initial_rows - final_rows} duplicate rows")
    
    # Convert date columns
    if 'Datahora' in df_cleaned.columns:
        try:
            df_cleaned['Datahora'] = pd.to_datetime(df_cleaned['Datahora'])
            print("Converted Datahora to datetime")
        except:
            print("Could not convert Datahora to datetime")
    
    print(f"Cleaned dataset: {df_cleaned.shape[0]} rows, {df_cleaned.shape[1]} columns")
    return df_cleaned

def save_datasets(merged_data, motorcycles_125cc_or_less, motorcycles_over_125cc):
    """Save all datasets to CSV files"""
    print("\nSaving datasets...")
    
    # Save merged and cleaned dataset
    merged_data.to_csv('merged_cleaned_accidents_2023.csv', index=False)
    print(f"Saved merged dataset: merged_cleaned_accidents_2023.csv ({merged_data.shape[0]} rows)")
    
    # Save motorcycle subsets
    motorcycles_125cc_or_less.to_csv('motorcycles_125cc_or_less_2023.csv', index=False)
    print(f"Saved motorcycles <= 125cc: motorcycles_125cc_or_less_2023.csv ({motorcycles_125cc_or_less.shape[0]} rows)")
    
    motorcycles_over_125cc.to_csv('motorcycles_over_125cc_2023.csv', index=False)
    print(f"Saved motorcycles > 125cc: motorcycles_over_125cc_2023.csv ({motorcycles_over_125cc.shape[0]} rows)")

def main():
    """Main function to execute the data processing pipeline"""
    print("=" * 60)
    print("TRAFFIC ACCIDENTS DATA PROCESSING 2023")
    print("=" * 60)
    
    try:
        # Load data
        acidentes, condutores, passageiros, peoes = load_and_examine_data()
        
        # Clean individual datasets first
        print("\nCleaning individual datasets...")
        acidentes_clean = clean_data(acidentes)
        condutores_clean = clean_data(condutores)
        passageiros_clean = clean_data(passageiros)
        peoes_clean = clean_data(peoes)
        
        # Merge datasets
        merged_data = clean_and_merge_data(acidentes_clean, condutores_clean, passageiros_clean, peoes_clean)
        
        # Final cleaning of merged data
        merged_data_clean = clean_data(merged_data)
        
        # Create motorcycle subsets
        motorcycles_125cc_or_less, motorcycles_over_125cc = create_motorcycle_subsets(merged_data_clean)
        
        # Clean motorcycle subsets
        if not motorcycles_125cc_or_less.empty:
            motorcycles_125cc_or_less = clean_data(motorcycles_125cc_or_less)
        
        if not motorcycles_over_125cc.empty:
            motorcycles_over_125cc = clean_data(motorcycles_over_125cc)
        
        # Save all datasets
        save_datasets(merged_data_clean, motorcycles_125cc_or_less, motorcycles_over_125cc)
        
        print("\n" + "=" * 60)
        print("DATA PROCESSING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        # Summary statistics
        print(f"\nFINAL SUMMARY:")
        print(f"- Total merged records: {merged_data_clean.shape[0]}")
        print(f"- Motorcycles <= 125cc: {motorcycles_125cc_or_less.shape[0]}")
        print(f"- Motorcycles > 125cc: {motorcycles_over_125cc.shape[0]}")
        
        # Show some basic statistics about motorcycle accidents
        if not motorcycles_125cc_or_less.empty or not motorcycles_over_125cc.empty:
            print(f"\nMOTORCYCLE ACCIDENT ANALYSIS:")
            
            if not motorcycles_125cc_or_less.empty:
                print(f"\nMotorcycles <= 125cc:")
                if 'Sexo' in motorcycles_125cc_or_less.columns:
                    print("Gender distribution:")
                    print(motorcycles_125cc_or_less['Sexo'].value_counts())
                
                if 'Lesões a 30 dias' in motorcycles_125cc_or_less.columns:
                    print("Injury severity:")
                    print(motorcycles_125cc_or_less['Lesões a 30 dias'].value_counts())
            
            if not motorcycles_over_125cc.empty:
                print(f"\nMotorcycles > 125cc:")
                if 'Sexo' in motorcycles_over_125cc.columns:
                    print("Gender distribution:")
                    print(motorcycles_over_125cc['Sexo'].value_counts())
                
                if 'Lesões a 30 dias' in motorcycles_over_125cc.columns:
                    print("Injury severity:")
                    print(motorcycles_over_125cc['Lesões a 30 dias'].value_counts())
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()