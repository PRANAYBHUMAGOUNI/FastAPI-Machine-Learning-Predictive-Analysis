from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import pandas as pd
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.impute import SimpleImputer

app = FastAPI()

# Global variables to hold the dataset and model
df = None
model = None

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Endpoint to upload CSV file
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global df
    try:
        contents = await file.read()
        # Reading the CSV file using pandas
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))

        # Validating the necessary columns existed
        required_columns = [
            'Date', 'Machine_ID', 'Assembly_Line_No', 
            'Hydraulic_Pressure(bar)', 'Coolant_Pressure(bar)',
            'Air_System_Pressure(bar)', 'Coolant_Temperature',
            'Hydraulic_Oil_Temperature(?C)', 'Spindle_Bearing_Temperature(?C)',
            'Spindle_Vibration(?m)', 'Tool_Vibration(?m)',
            'Spindle_Speed(RPM)', 'Voltage(volts)', 'Torque(Nm)',
            'Cutting(kN)', 'Downtime'
        ]
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail="CSV file missing required columns.")

        # Handling missing values: Imputing numerical columns with mean
        imputer = SimpleImputer(strategy='mean')

        # Imputing all numeric features first before converting Downtime
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

        # Converting 'Downtime' column to binary 
        df['Downtime'] = df['Downtime'].apply(lambda x: 1 if x == 'Machine_Failure' else 0)

        return {"message": "File uploaded successfully", "columns": list(df.columns)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

# Endpoint to train the model
@app.post("/train")
def train_model():
    global model, df

    if df is None:
        raise HTTPException(status_code=400, detail="No data uploaded. Please upload a CSV file first.")

    try:
        # Selecting features and target variable
        X = df[['Hydraulic_Pressure(bar)', 'Coolant_Pressure(bar)', 'Air_System_Pressure(bar)',
                'Coolant_Temperature', 'Hydraulic_Oil_Temperature(?C)',
                'Spindle_Bearing_Temperature(?C)', 'Spindle_Vibration(?m)',
                'Tool_Vibration(?m)', 'Spindle_Speed(RPM)', 'Voltage(volts)',
                'Torque(Nm)', 'Cutting(kN)']]
        y = df['Downtime']

        # Splitting data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Training Logistic Regression model
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Evaluating the model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        return {"message": "Model trained successfully", "accuracy": accuracy, "f1_score": f1}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error training model: {str(e)}")

# Requesting model for predictions
class PredictRequest(BaseModel):
    Hydraulic_Pressure_bar: float
    Coolant_Pressure_bar: float
    Air_System_Pressure_bar: float
    Coolant_Temperature: float
    Hydraulic_Oil_Temperature_C: float
    Spindle_Bearing_Temperature_C: float
    Spindle_Vibration_m: float
    Tool_Vibration_m: float
    Spindle_Speed_RPM: int
    Voltage_volts: float
    Torque_Nm: float
    Cutting_kN: float

# Endpoint to make predictions
@app.post("/predict")
def predict(data: PredictRequest):
    global model

    if model is None:
        raise HTTPException(status_code=400, detail="Model not trained. Please train the model first.")

    try:
        # Extracting input features from request data
        input_data = [
            data.Hydraulic_Pressure_bar,
            data.Coolant_Pressure_bar,
            data.Air_System_Pressure_bar,
            data.Coolant_Temperature,
            data.Hydraulic_Oil_Temperature_C,
            data.Spindle_Bearing_Temperature_C,
            data.Spindle_Vibration_m,
            data.Tool_Vibration_m,
            data.Spindle_Speed_RPM,
            data.Voltage_volts,
            data.Torque_Nm,
            data.Cutting_kN
        ]

        # Making predictions using the trained model
        prediction = model.predict([input_data])
        confidence = max(model.predict_proba([input_data])[0])

        return {
            "Downtime": "Yes" if prediction[0] == 1 else "No",
            "Confidence": confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {str(e)}")

