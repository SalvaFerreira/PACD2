import pandas as pd

def verify_results():
    """Verify the results of the data processing"""
    print("=" * 60)
    print("VERIFICATION OF PROCESSED DATA")
    print("=" * 60)
    
    # Load the processed files
    try:
        merged_data = pd.read_csv('merged_cleaned_accidents_2023.csv')
        motorcycles_125cc = pd.read_csv('motorcycles_125cc_or_less_2023.csv')
        motorcycles_over_125cc = pd.read_csv('motorcycles_over_125cc_2023.csv')
        
        print(f"\n📊 DATASET SUMMARY:")
        print(f"- Merged dataset: {merged_data.shape[0]:,} rows, {merged_data.shape[1]} columns")
        print(f"- Motorcycles ≤ 125cc: {motorcycles_125cc.shape[0]:,} rows")
        print(f"- Motorcycles > 125cc: {motorcycles_over_125cc.shape[0]:,} rows")
        
        print(f"\n🏍️ MOTORCYCLE ACCIDENT ANALYSIS:")
        
        # Analysis for motorcycles <= 125cc
        if not motorcycles_125cc.empty:
            print(f"\n--- Motorcycles ≤ 125cc ---")
            print(f"Total accidents: {motorcycles_125cc.shape[0]:,}")
            
            if 'Sexo' in motorcycles_125cc.columns:
                print("\nGender distribution:")
                gender_dist = motorcycles_125cc['Sexo'].value_counts()
                for gender, count in gender_dist.items():
                    print(f"  {gender}: {count:,} ({count/len(motorcycles_125cc)*100:.1f}%)")
            
            if 'Lesões a 30 dias' in motorcycles_125cc.columns:
                print("\nInjury severity:")
                injury_dist = motorcycles_125cc['Lesões a 30 dias'].value_counts()
                for injury, count in injury_dist.items():
                    print(f"  {injury}: {count:,} ({count/len(motorcycles_125cc)*100:.1f}%)")
            
            if 'Mês' in motorcycles_125cc.columns:
                print("\nTop 5 months with most accidents:")
                month_dist = motorcycles_125cc['Mês'].value_counts().head()
                for month, count in month_dist.items():
                    print(f"  {month}: {count:,}")
        
        # Analysis for motorcycles > 125cc
        if not motorcycles_over_125cc.empty:
            print(f"\n--- Motorcycles > 125cc ---")
            print(f"Total accidents: {motorcycles_over_125cc.shape[0]:,}")
            
            if 'Sexo' in motorcycles_over_125cc.columns:
                print("\nGender distribution:")
                gender_dist = motorcycles_over_125cc['Sexo'].value_counts()
                for gender, count in gender_dist.items():
                    print(f"  {gender}: {count:,} ({count/len(motorcycles_over_125cc)*100:.1f}%)")
            
            if 'Lesões a 30 dias' in motorcycles_over_125cc.columns:
                print("\nInjury severity:")
                injury_dist = motorcycles_over_125cc['Lesões a 30 dias'].value_counts()
                for injury, count in injury_dist.items():
                    print(f"  {injury}: {count:,} ({count/len(motorcycles_over_125cc)*100:.1f}%)")
            
            if 'Mês' in motorcycles_over_125cc.columns:
                print("\nTop 5 months with most accidents:")
                month_dist = motorcycles_over_125cc['Mês'].value_counts().head()
                for month, count in month_dist.items():
                    print(f"  {month}: {count:,}")
        
        # Comparison
        print(f"\n📈 COMPARISON:")
        total_motorcycle_accidents = len(motorcycles_125cc) + len(motorcycles_over_125cc)
        print(f"Total motorcycle accidents: {total_motorcycle_accidents:,}")
        print(f"≤ 125cc represents {len(motorcycles_125cc)/total_motorcycle_accidents*100:.1f}% of motorcycle accidents")
        print(f"> 125cc represents {len(motorcycles_over_125cc)/total_motorcycle_accidents*100:.1f}% of motorcycle accidents")
        
        print(f"\n✅ FILES CREATED:")
        print(f"- merged_cleaned_accidents_2023.csv")
        print(f"- motorcycles_125cc_or_less_2023.csv")
        print(f"- motorcycles_over_125cc_2023.csv")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_results()