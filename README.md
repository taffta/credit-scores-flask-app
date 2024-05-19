# Credit Score Prediction Web Application

This project is a web application built using Flask that predicts credit scores based on user input features. The application uses a pre-trained machine learning model to perform the predictions.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example cURL Command](#example-curl-command)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/credit-score-prediction.git
    cd credit-score-prediction
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure the pre-trained model file is in the project directory:**
    Place the model file `credit scores best model` in the project root directory.

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**
    ```
    http://localhost:5000
    ```

3. **Use the web form to input features and predict the credit score.**

## Endpoints

### `/`
- **Method:** `GET`
- **Description:** Renders the index page with the input form.

### `/predict`
- **Method:** `POST`
- **Description:** Receives a JSON payload with feature values, performs prediction, and returns the predicted credit score.
- **Payload Example:**
    ```json
    {
        "Month": "1",
        "Age": "35",
        "Occupation": "Engineer",
        "Annual_Income": "50000",
        "Monthly_Inhand_Salary": "4000",
        "Num_Bank_Accounts": "2",
        "Num_Credit_Card": "2",
        "Interest_Rate": "6.5",
        "Delay_from_due_date": "15",
        "Num_of_Delayed_Payment": "2",
        "Changed_Credit_Limit": "50000",
        "Num_Credit_Inquiries": "2",
        "Credit_Mix": "0",
        "Outstanding_Debt": "15000",
        "Credit_Utilization_Ratio": "20000",
        "Credit_History_Age": "0.5",
        "Payment_of_Min_Amount": "5",
        "Total_EMI_per_month": "1000",
        "Amount_invested_monthly": "500",
        "Payment_Behaviour": "Good",
        "Monthly_Balance": "500",
        "Count_Auto Loan": "1",
        "Count_Credit-Builder Loan": "0",
        "Count_Personal Loan": "0",
        "Count_Home Equity Loan": "0",
        "Count_Not Specified": "1",
        "Count_Mortgage Loan": "0",
        "Count_Student Loan": "0",
        "Count_Debt Consolidation Loan": "0",
        "Count_Payday Loan": "0"
    }
    ```

## Example cURL Command

To test the `/predict` endpoint using cURL, you can use the following command:

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "Month": "1",
  "Age": "35",
  "Occupation": "Engineer",
  "Annual_Income": "50000",
  "Monthly_Inhand_Salary": "4000",
  "Num_Bank_Accounts": "2",
  "Num_Credit_Card": "2",
  "Interest_Rate": "6.5",
  "Delay_from_due_date": "15",
  "Num_of_Delayed_Payment": "2",
  "Changed_Credit_Limit": "50000",
  "Num_Credit_Inquiries": "2",
  "Credit_Mix": "0",
  "Outstanding_Debt": "15000",
  "Credit_Utilization_Ratio": "20000",
  "Credit_History_Age": "0.5",
  "Payment_of_Min_Amount": "5",
  "Total_EMI_per_month": "1000",
  "Amount_invested_monthly": "500",
  "Payment_Behaviour": "Good",
  "Monthly_Balance": "500",
  "Count_Auto Loan": "1",
  "Count_Credit-Builder Loan": "0",
  "Count_Personal Loan": "0",
  "Count_Home Equity Loan": "0",
  "Count_Not Specified": "1",
  "Count_Mortgage Loan": "0",
  "Count_Student Loan": "0",
  "Count_Debt Consolidation Loan": "0",
  "Count_Payday Loan": "0"
}'
