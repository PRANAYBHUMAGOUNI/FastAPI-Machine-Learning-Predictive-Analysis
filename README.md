# Machine Downtime Prediction using FastAPI and Logistic Regression

## Project Overview
This project is a machine learning application built with FastAPI that predicts machine downtime using logistic regression. Users can upload machine performance datasets, train a predictive model, and make real-time predictions about potential machine failures using Postman.

## Dataset Description

### Dataset Overview

**Total Rows:** 2,500
**Total Columns:** 16

### Sample Data

The sample data contains various machine parameters recorded at different times. Below is an sample of the dataset:

| Date       | Machine_ID         | Assembly_Line_No | Hydraulic_Pressure(bar) | Coolant_Pressure(bar) | Air_System_Pressure(bar) | Coolant_Temperature | Hydraulic_Oil_Temperature(°C) | Spindle_Bearing_Temperature(°C) | Spindle_Vibration(m) | Tool_Vibration(m) | Spindle_Speed(RPM) | Voltage(volts) | Torque(Nm) | Cutting(kN) | Downtime        |
|------------|--------------------|------------------|-------------------------|-----------------------|--------------------------|--------------------|------------------------------|---------------------------------|----------------------|-------------------|-------------------|----------------|------------|-------------|-----------------|
| 31-12-2021 | Makino-L1-Unit1-2013 | Shopfloor-L1     | 71.04                   | 6.9337                | 6.285                    | 25.6               | 46                           | 33.4                            | 1.291                | 26.492            | 25892             | 335            | 24.06      | 3.58        | Machine_Failure |
| 31-12-2021 | Makino-L1-Unit1-2013 | Shopfloor-L1     | 125.33                  | 4.9369                | 6.197                    | 35.3               | 47.4                         | 34.6                            | 1.382                | 25.274            | 19856             | 368            | 14.20      | 2.68        | Machine_Failure |
| 31-12-2021 | Makino-L3-Unit1-2015 | Shopfloor-L3     | 71.12                   | 6.8394                | 6.655                    | 13.1               | 40.7                         | 33                              | 1.319                | 30.608            | 19851             | 325            | 24.05      | 3.55        | Machine_Failure |
| 31-05-2022 | Makino-L2-Unit1-2015 | Shopfloor-L2     | 139.34                  | 4.5744                | 6.560                    | 24.4               | 44.2                         | 40.6                            | 0.618                | 30.791            | 18461             | 360            | 25.86      | 3.55        | Machine_Failure |
| 31-03-2022 | Makino-L1-Unit1-2013 | Shopfloor-L1     | 60.51                   | 6.8932                | 6.141                    | 4.1                | 47.3                         | 31.4                            | 0.983                | 25.516            | 26526             | 354            | 25.52      | 3.55        | Machine_Failure |
| 31-03-2022 | Makino-L2-Unit1-2015 | Shopfloor-L2     | 137.37                  | 5.9184                | 7.228                    | 5.4                | 48                           | 32.7                            | 0.903                | 25.597            | 27613             | 319            | 25.52      | 3.55        | Machine_Failure |
| 31-03-2022 | Makino-L1-Unit1-2013 | Shopfloor-L1     | 135.93                  | 6.5603                | 6.711                    | 19.3               | 48.8                         | 37.4                            | 1.24                 | 32.138            | 26605             | 438            | 25.45      | 3.58        | Machine_Failure |
| 31-03-2022 | Makino-L3-Unit1-2015 | Shopfloor-L3     | 127.72                  | 5.0607                | 6.002                    | 20.8               | 45.8                         | 37.5                            | 1.125                | 19.823            | 14266             | 334            | 34.97      | 2.02        | No_Machine_Failure |
| 31-03-2022 | Makino-L3-Unit1-2015 | Shopfloor-L3     | 123.62                  | 5.0744                | 6.039                    | 4.5                | 51.5                         | 32.1                            | 0.69                 | 16.972            | 20413             | 278            | 32.52      | 2.88        | No_Machine_Failure |



### Columns and Their Meanings
1. **Date**: Recording date of machine performance data
2. **Machine_ID**: Unique identifier for each machine
3. **Assembly_Line_No**: Location or line of the machine
4. **Hydraulic_Pressure(bar)**: Hydraulic system pressure measurement
5. **Coolant_Pressure(bar)**: Cooling system pressure measurement
6. **Air_System_Pressure(bar)**: Compressed air system pressure
7. **Coolant_Temperature**: Temperature of the cooling system
8. **Hydraulic_Oil_Temperature(?C)**: Temperature of hydraulic oil
9. **Spindle_Bearing_Temperature(?C)**: Temperature of spindle bearings
10. **Spindle_Vibration(?m)**: Vibration measurement of spindle
11. **Tool_Vibration(?m)**: Vibration measurement of tools
12. **Spindle_Speed(RPM)**: Rotational speed of spindle
13. **Voltage(volts)**: Electrical voltage
14. **Torque(Nm)**: Rotational force measurement
15. **Cutting(kN)**: Cutting force
16. **Downtime**: Machine failure status (Machine_Failure/No_Machine_Failure)

## Requirements
- Python 3.8+
- FastAPI
- Pandas
- Scikit-learn
- Uvicorn
- Postman

## Installation

1. Clone the repository
```bash
git clone https://github.com/PRANAYBHUMAGOUNI/FastAPI-Machine-Learning-Predictive-Analysis.git
cd FastAPI-Machine-Learning-Predictive-Analysis
```

2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application with Postman

1. Start the FastAPI server
```bash
uvicorn main:app --reload --port 8000
```

2. Open Postman and use these endpoints:

### A. Root Endpoint
- **URL**: `http://127.0.0.1:8000/`
- **Method**: GET
- **Expected Response**: 
  ```json
  {"message":"Welcome to the FastAPI application!"}
  ```

### B. Upload Dataset
- **URL**: `http://127.0.0.1:8000/upload`
- **Method**: POST
- **Body**: Select 'form-data', choose 'file' type, and upload your CSV

### C. Train Model
- **URL**: `http://127.0.0.1:8000/train`
- **Method**: POST
- **Expected Response**: 
  ```json
  {
    "message": "Model trained successfully", 
    "accuracy": 0.84, 
    "f1_score": 0.8283
  }
  ```

### D. Predict Downtime
- **URL**: `http://127.0.0.1:8000/predict`
- **Method**: POST
- **Body**: Raw JSON
  ```json
  {
    "Hydraulic_Pressure_bar": 125.0,
    "Coolant_Pressure_bar": 5.0,
    "Air_System_Pressure_bar": 6.0,
    "Coolant_Temperature": 22.0,
    "Hydraulic_Oil_Temperature_C": 45.0,
    "Spindle_Bearing_Temperature_C": 30.0,
    "Spindle_Vibration_m": 0.5,
    "Tool_Vibration_m": 0.3,
    "Spindle_Speed_RPM": 21000,
    "Voltage_volts": 380.0,
    "Torque_Nm": 20.0,
    "Cutting_kN": 2.5
  }
  ```
- **Expected Response**:
  ```json
  {
    "Downtime": "No",
    "Confidence": 0.774
  }
  ```

## Model Performance
- **Accuracy**: 84%
- **F1 Score**: 0.828

## Results Screenshots

**Root Endpoint**:
![image](https://github.com/user-attachments/assets/bcdf1b01-49b0-47b1-8928-092ceb420b97)

**Upload Dataset**:
![image](https://github.com/user-attachments/assets/1d273c7c-af69-4feb-b9ae-f47e6829ef0a)

**Train Model**:
![image](https://github.com/user-attachments/assets/72641d62-a6bb-462d-ab59-9701ccd28850)

**Predict Downtime**:
![image](https://github.com/user-attachments/assets/4c0165ad-f1e9-4e24-9573-8b8cb7a9b71c)


![image](https://github.com/user-attachments/assets/af3e4986-00aa-4c63-bff5-b30a9236b524)


