# Machine Downtime Prediction using FastAPI and Logistic Regression

## Project Overview
This project is a machine learning application built with FastAPI that predicts machine downtime using logistic regression. Users can upload machine performance datasets, train a predictive model, and make real-time predictions about potential machine failures using Postman.

## Dataset Description

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


