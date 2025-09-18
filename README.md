# Traffic Accidents Data Analysis 2023 🚗📊

A comprehensive Python project for merging, cleaning, and analyzing Portuguese traffic accident data from 2023, with special focus on motorcycle accidents by engine capacity.

## 📋 Project Overview

This project processes four different CSV datasets containing traffic accident information from Portugal in 2023:
- **Accidents** (`acidentes_2023.csv`) - Main accident records
- **Drivers** (`condutores_2023.csv`) - Driver information
- **Passengers** (`passageiros_2023.csv`) - Passenger details  
- **Pedestrians** (`peões_2023.csv`) - Pedestrian involvement

The main goal is to merge these datasets and create specialized subsets focusing on motorcycle accidents categorized by engine capacity (≤ 125cc vs > 125cc).

## 🎯 Key Features

- **Data Merging**: Combines multiple related datasets using common identifiers
- **Data Cleaning**: Handles missing values, duplicates, and data type conversions
- **Motorcycle Analysis**: Creates specific subsets for different motorcycle categories
- **Statistical Summary**: Provides comprehensive analysis of accident patterns
- **Export Functionality**: Saves processed data to new CSV files

## 📈 Key Findings

### Motorcycle Accidents Summary (2023)
- **Total motorcycle accidents**: 9,449
- **≤ 125cc motorcycles**: 5,522 accidents (58.4%)
- **> 125cc motorcycles**: 3,927 accidents (41.6%)

### Safety Insights
- **Fatality rates**: Higher motorcycles (> 125cc) show 2.6% fatality rate vs 0.8% for smaller ones
- **Gender distribution**: 96.5% male riders for > 125cc vs 87.8% for ≤ 125cc
- **Peak months**: Summer months (July-August) show highest accident rates

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/traffic-accidents-analysis-2023.git
   cd traffic-accidents-analysis-2023
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install pandas numpy
   ```

## 🚀 Usage

### Basic Usage

1. **Place your CSV files** in the project directory:
   - `acidentes_2023.csv`
   - `condutores_2023.csv`
   - `passageiros_2023.csv`
   - `peões_2023.csv`

2. **Run the main processing script**:
   ```bash
   python merge_and_clean_data.py
   ```

3. **Verify results**:
   ```bash
   python verify_results.py
   ```

### Output Files

The script generates three main output files:

- **`merged_cleaned_accidents_2023.csv`** - Complete merged dataset
- **`motorcycles_125cc_or_less_2023.csv`** - Motorcycles ≤ 125cc subset
- **`motorcycles_over_125cc_2023.csv`** - Motorcycles > 125cc subset

## 📊 Data Structure

### Input Datasets
- **Accidents**: 36,597 rows, 46 columns (accident details, location, conditions)
- **Drivers**: 59,662 rows, 38 columns (driver info, vehicle details, age groups)
- **Passengers**: 9,676 rows, 25 columns (passenger information and injuries)
- **Pedestrians**: 5,113 rows, 25 columns (pedestrian involvement and injuries)

### Merged Dataset
- **Final merged data**: 61,862 rows, 129 columns
- **Key relationships**: Linked by accident ID and vehicle ID
- **Data quality**: Cleaned for duplicates and missing values

## 🔍 Analysis Features

### Motorcycle Accident Analysis
- Engine capacity categorization (≤ 125cc vs > 125cc)
- Gender distribution analysis
- Injury severity patterns
- Temporal analysis (monthly trends)
- Geographic distribution (districts/regions)

### Statistical Insights
- Injury severity comparison between motorcycle types
- Age group analysis
- Seasonal accident patterns
- Safety equipment usage correlation

## 📁 File Structure

```
traffic-accidents-analysis-2023/
│
├── merge_and_clean_data.py      # Main processing script
├── verify_results.py            # Results verification script
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
│
├── Input Files (you provide):
├── acidentes_2023.csv           # Accident records
├── condutores_2023.csv          # Driver information
├── passageiros_2023.csv         # Passenger details
├── peões_2023.csv               # Pedestrian data
│
└── Output Files (generated):
    ├── merged_cleaned_accidents_2023.csv
    ├── motorcycles_125cc_or_less_2023.csv
    └── motorcycles_over_125cc_2023.csv
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Portuguese traffic safety authorities for providing the data
- Python community for excellent data analysis libraries (pandas, numpy)
- Contributors and users of this analysis tool

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please feel free to:
- Open an issue on GitHub
- Contact the maintainer: [your.email@example.com]

---

**Note**: This project is for educational and research purposes. Always refer to official traffic safety sources for policy decisions.