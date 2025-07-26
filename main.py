import pandas as pd
import matplotlib.pyplot as plt
import os

class Main:
    def __init__(self) -> None:
        # Create directory for saving plots
        os.makedirs('./plots', exist_ok=True)
    
    def structure_data(self, df) -> None:
        """Check the structure of the data."""
        print('=' * 100)
        print(f'Shape of dataset:\n{df.shape}\n')
        print("First 5 rows:")
        print(df.head())

    def type_check(self, df) -> None:
        """Check data types and descriptive stats."""
        print('=' * 100)
        print(f'Data types:\n{df.dtypes}\n')
        print(f'Descriptive statistics:\n{df.describe(percentiles=[0.25, 0.5, 0.75])}\n')

    def quality(self, df) -> None:
        """Assess data quality."""
        print('=' * 100)
        print(f'Null values:\n{df.isnull().sum()}\n')
        print(f'Duplicate rows: {df.duplicated().sum()}')

    def load_csv(self):
        """Load the enhanced dataset from path."""
        return pd.read_csv('./Dataset/uber.csv')

    def handle_missing(self, data):
        """Handle missing values."""
        # Fill missing values for relevant columns (for enhanced dataset)
        data = data.fillna({
            'dropoff_longitude': 0,
            'dropoff_latitude': 0,
            'pickup_longitude': 0,
            'pickup_latitude': 0,
            'distance_km': 0  
        }).drop_duplicates()
        return data
    
    def ead(self, data):
        """Plot histogram of fare_amount."""
        plt.figure(figsize=(10, 6))
        plt.hist(data['fare_amount'], bins=30)
        plt.title('Distribution of Fare Amounts')
        plt.xlabel('Fare Amount ($)')
        plt.ylabel('Frequency')
        plt.savefig('./plots/fare_distribution.png')
        plt.close()
    
    def plot_fare_vs_distance(self, data):
        """Plot fare vs. distance using simplified approximation."""
        if 'distance_km' not in data.columns:
            data['distance_km'] = data.apply(
                lambda row: self.haversine_approx(
                    row['pickup_latitude'],
                    row['pickup_longitude'],
                    row['dropoff_latitude'],
                    row['dropoff_longitude']
                ),
                axis=1
            )

        plt.figure(figsize=(10, 6))
        plt.scatter(data['distance_km'], data['fare_amount'], alpha=0.5)
        plt.title('Fare Amount vs. Approximate Distance')
        plt.xlabel('Approximate Distance (km)')
        plt.ylabel('Fare ($)')
        plt.savefig('./plots/fare_vs_distance.png')
        plt.close()

    def haversine_approx(self, lat1, lon1, lat2, lon2):
        """Simplified Haversine-like approximation (no trig functions)."""
        dx = (lon2 - lon1) * 85  # ~85 km per degree longitude (near NYC)
        dy = (lat2 - lat1) * 111  # ~111 km per degree latitude
        return (dx**2 + dy**2) ** 0.5

    def plot_fare_by_hour(self, data):
        """Plot fare by hour by extracting hour from pickup_datetime."""
        # First convert pickup_datetime to datetime format if it's not already
        if not pd.api.types.is_datetime64_any_dtype(data['pickup_datetime']):
            data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
        
        # Extract hour from datetime
        data['hour'] = data['pickup_datetime'].dt.hour
        
        # Now group by hour
        avg_fare = data.groupby('hour')['fare_amount'].mean()
        
        plt.figure(figsize=(10, 6))
        avg_fare.plot(kind='line', marker='o')
        plt.title('Average Fare by Hour of Day')
        plt.xlabel('Hour')
        plt.ylabel('Average Fare ($)')
        plt.grid()
        plt.savefig('./plots/fare_by_hour.png')
        plt.close()

    def run(self):
        """Main execution flow."""
        data = self.load_csv()
        self.structure_data(data)
        self.type_check(data)
        self.quality(data)
        
        clean_data = self.handle_missing(data)
        print("\nAfter handling missing values:")
        self.quality(clean_data)

        # Export cleaned data
        clean_data.to_csv('./Dataset/uber_cleaned.csv', index=False)
        print("\nCleaned data exported to 'uber_cleaned.csv'.")

        # Generate and save visualizations
        self.ead(clean_data)
        self.plot_fare_vs_distance(clean_data)
        self.plot_fare_by_hour(clean_data)
        
        # Calculate statistics
        helper(clean_data)

def helper(data) -> None:
    """External helper for descriptive stats and outliers."""
    numeric_data = data.select_dtypes(include=['number'])
    
    # Basic statistics
    print('Mean values:\n', numeric_data.mean(), '\n')
    print('Mode values:\n', numeric_data.mode().iloc[0] if not numeric_data.mode().empty else "No mode", '\n')
    print('Standard deviation:\n', numeric_data.std(), '\n')
    
    # Quantiles and range
    quantiles = numeric_data.quantile([0.25, 0.5, 0.75])
    print('Quantiles:\n', quantiles, '\n')
    print('Range:\n', numeric_data.max() - numeric_data.min(), '\n')
    
    # Outliers
    iqr = quantiles.loc[0.75] - quantiles.loc[0.25]
    lower_bound = quantiles.loc[0.25] - 1.5 * iqr
    upper_bound = quantiles.loc[0.75] + 1.5 * iqr
    
    outliers = data[((numeric_data < lower_bound) | (numeric_data > upper_bound)).any(axis=1)]
    print(f'Outliers detected ({len(outliers)} rows):\n', outliers.head())


if __name__ == "__main__":
    Main().run()
