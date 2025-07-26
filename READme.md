### Introduction
downaload dataset on kaggle
python -m venv myenv
pip install pandas


# 🚖 **Uber Fares Dataset Analysis using Power BI** 📊

## Project Overview 📝

This project involves an in-depth analysis of the **Uber Fares Dataset** to uncover insights into fare amounts, ride durations, and various operational metrics. I’ve used **Power BI** to create an interactive dashboard that visually represents these findings and provides data-driven recommendations for improving Uber's operational strategies.

---

## **Methodology** 🔧

### 1. **Data Collection and Preparation** 📥

* **Dataset Source**: The dataset was downloaded from Kaggle: [Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset).
* **Data Loading**: Loaded the dataset into **Python** using **Pandas** for initial exploration and data cleaning.
* **Data Cleaning**: Handled missing values, identified and managed outliers, and applied necessary transformations.
* **Feature Engineering**: Extracted new features such as **hour**, **day**, **month**, and **day of the week** from timestamps.
* **Export for Power BI**: Saved the cleaned data as a **CSV** file, which was later imported into **Power BI**.

---

### 2. **Exploratory Data Analysis (EDA)** 🔍

* **Descriptive Statistics**: Computed the **mean**, **median**, **mode**, **standard deviation**, and **quartiles**.
* **Fare Distribution**: Created **visualizations** such as histograms and box plots to understand fare distribution.
* **Correlation Analysis**: Analyzed relationships between variables like fare amount and distance, time of day, and duration.

**Fare Distribution Visual**
![Fare Distribution by Day, Hour, Weekday, Month](https://raw.githubusercontent.com/Aimable2002/big_data_sign/main/powerBI/fare.png)

*This visual shows fare patterns across different days, hours, months, and weekdays.*

### 3. **Feature Engineering** 🛠️

* **Timestamp Extraction**: Created features such as **hour**, **day**, **month**, and **day of the week** to analyze temporal trends.
* **Categorical Encoding**: Categorical variables were encoded for Power BI analysis.
* **Peak/Off-Peak Indicators**: Identified peak and off-peak times to provide a better understanding of demand periods.

---

## **Data Analysis in Power BI** 💡

### Key Visualizations:

* **Fare Distribution**: Fare amounts were visualized using histograms and box plots.
* **Ride Duration**: Time-based analysis of ride durations.
* **Time Series Analysis**: Analyzed temporal patterns, showing peaks during specific hours, days, and months.

**Time-based Pattern Visual**
![Average Fare by Hour](https://raw.githubusercontent.com/Aimable2002/big_data_sign/main/plots/fare_by_hour.png)

*This chart visualizes how the average fare amount varies by hour of the day.*

![Pickup Location Distribution](https://raw.githubusercontent.com/Aimable2002/big_data_sign/main/powerBI/pick.png)

*This chart visualizes how the average fare amount varies by hour of the day. and counts of pickup date*

---

## **Results** 🎯

The analysis produced key insights into Uber fare patterns and ride frequencies:

1. **Peak Fare Periods**: Late nights and early mornings exhibit higher fare amounts due to surge pricing and demand.
2. **Busiest Days**: Weekdays, especially Thursdays and Fridays, experienced the highest number of rides.
3. **Fare Fluctuations**: Fare amounts were significantly higher in December due to holiday demand.
4. **Ride Duration Insights**: The average ride duration varies based on the time of day, with longer trips occurring during certain hours.

---


## **Conclusion** 🏁

The **Uber Fares Dataset** analysis has provided valuable insights into **fare patterns**, **ride frequencies**, and **peak demand periods**. The **interactive Power BI dashboard** allows Uber to visualize and make strategic decisions based on the data-driven findings. By optimizing pricing strategies and targeting specific periods and regions, Uber can enhance its operational efficiency and customer experience.

---

## **Dashboard For Summary** 📸

![Dashboard](https://raw.githubusercontent.com/Aimable2002/big_data_sign/main/powerBI/Dashboard.png)

---


## **Terminal Output Logs** 💻

Below is the actual terminal output after running the `main.py` script in your virtual environment (`myenv`):

```bash
(myenv) C:\Users\ISO\Desktop\bigdata_assign>python main.py
====================================================================================================
Shape of dataset:
(200000, 9)

First 5 rows:
   Unnamed: 0                            key  fare_amount  ... dropoff_longitude  dropoff_latitude  passenger_count
0    24238194    2015-05-07 19:52:06.0000003          7.5  ...        -73.999512         40.723217                1
1    27835199    2009-07-17 20:04:56.0000002          7.7  ...        -73.994710         40.750325                1
2    44984355   2009-08-24 21:45:00.00000061         12.9  ...        -73.962565         40.772647                1
3    25894730    2009-06-26 08:22:21.0000001          5.3  ...        -73.965316         40.803349                3
4    17610152  2014-08-28 17:47:00.000000188         16.0  ...        -73.973082         40.761247                5

[5 rows x 9 columns]
====================================================================================================
Data types:
Unnamed: 0             int64
key                   object
fare_amount          float64
pickup_datetime       object
pickup_longitude     float64
pickup_latitude      float64
dropoff_longitude    float64
dropoff_latitude     float64
passenger_count        int64
dtype: object

Descriptive statistics:
         Unnamed: 0    fare_amount  pickup_longitude  ...  dropoff_longitude  dropoff_latitude  passenger_count
count  2.000000e+05  200000.000000     200000.000000  ...      199999.000000     199999.000000    200000.000000
mean   2.771250e+07      11.359955        -72.527638  ...         -72.525292         39.923890         1.684535
std    1.601382e+07       9.901776         11.437787  ...          13.117408          6.794829         1.385997
min    1.000000e+00     -52.000000      -1340.648410  ...       -3356.666300       -881.985513         0.000000
25%    1.382535e+07       6.000000        -73.992065  ...         -73.991407         40.733823         1.000000
50%    2.774550e+07       8.500000        -73.981823  ...         -73.980093         40.753042         1.000000
75%    4.155530e+07      12.500000        -73.967154  ...         -73.963658         40.768001         2.000000
max    5.542357e+07     499.000000         57.418457  ...        1153.572603        872.697628       208.000000

[8 rows x 7 columns]
====================================================================================================
Null values:
Unnamed: 0           0
key                  0
fare_amount          0
pickup_datetime      0
pickup_longitude     0
pickup_latitude      0
dropoff_longitude    1
dropoff_latitude     1
passenger_count      0
dtype: int64

Duplicate rows: 0

After handling missing values:
====================================================================================================
Null values:
Unnamed: 0           0
key                  0
fare_amount          0
pickup_datetime      0
pickup_longitude     0
pickup_latitude      0
dropoff_longitude    0
dropoff_latitude     0
passenger_count      0
dtype: int64

Duplicate rows: 0

Cleaned data exported to 'uber_cleaned.csv'.
Mean values:
 Unnamed: 0           2.771250e+07
fare_amount          1.135996e+01
pickup_longitude    -7.252764e+01
pickup_latitude      3.993589e+01
dropoff_longitude   -7.252493e+01
dropoff_latitude     3.992369e+01
passenger_count      1.684535e+00
distance_km          2.388263e+01
hour                 1.349133e+01
dtype: float64

Mode values:
 Unnamed: 0            1.0
fare_amount           6.5
pickup_longitude      0.0
pickup_latitude       0.0
dropoff_longitude     0.0
dropoff_latitude      0.0
passenger_count       1.0
distance_km           0.0
hour                 19.0
Name: 0, dtype: float64

Standard deviation:
 Unnamed: 0           1.601382e+07
fare_amount          9.901776e+00
pickup_longitude     1.143779e+01
pickup_latitude      7.720539e+00
dropoff_longitude    1.311838e+01
dropoff_latitude     6.795398e+00
passenger_count      1.385997e+00
distance_km          8.817159e+02
hour                 6.515531e+00
dtype: float64

Quantiles:
        Unnamed: 0  fare_amount  pickup_longitude  pickup_latitude  ...  dropoff_latitude  passenger_count  distance_km  hour
0.25  13825346.25          6.0        -73.992065        40.734796  ...         40.733823              1.0     1.219105   9.0
0.50  27745495.00          8.5        -73.981823        40.752592  ...         40.753042              1.0     2.127005  14.0
0.75  41555300.75         12.5        -73.967154        40.767158  ...         40.768001              2.0     3.881083  19.0

[3 rows x 9 columns]

Range:
 Unnamed: 0           5.542357e+07
fare_amount          5.510000e+02
pickup_longitude     1.398067e+03
pickup_latitude      1.718437e+03
dropoff_longitude    4.510239e+03
dropoff_latitude     1.754683e+03
passenger_count      2.080000e+02
distance_km          2.586769e+05
hour                 2.300000e+01
dtype: float64

Outliers detected (50271 rows):
     Unnamed: 0                            key  fare_amount  ... passenger_count  distance_km  hour
4     17610152  2014-08-28 17:47:00.000000188         16.0  ...               5     4.507361    17
6     48725865    2014-10-12 07:04:00.0000002         24.5  ...               5    11.762692     7
7     44195482   2012-12-11 13:52:00.00000029          2.5  ...               1     0.000000    13
11     6379048   2011-05-23 22:15:00.00000086          8.5  ...               1     0.000000    22
12    31892535  2011-05-17 14:03:00.000000158          3.3  ...               5     0.301787    14

[5 rows x 11 columns]

(myenv) C:\Users\ISO\Desktop\bigdata_assign>

```

