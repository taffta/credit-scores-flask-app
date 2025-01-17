from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Loading the model
model = joblib.load('credit scores best model')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extracting features from the received data
        features = [
            data['Month'],
            data['Age'],
            data['Occupation'],
            data['Annual_Income'],
            data['Monthly_Inhand_Salary'],
            data['Num_Bank_Accounts'],
            data['Num_Credit_Card'],
            data['Interest_Rate'],
            data['Delay_from_due_date'],
            data['Num_of_Delayed_Payment'],
            data['Changed_Credit_Limit'],
            data['Num_Credit_Inquiries'],
            data['Credit_Mix'],
            data['Outstanding_Debt'],
            data['Credit_Utilization_Ratio'],
            data['Credit_History_Age'],
            data['Payment_of_Min_Amount'],
            data['Total_EMI_per_month'],
            data['Amount_invested_monthly'],
            data['Payment_Behaviour'],
            data['Monthly_Balance'],
            data['Count_Auto Loan'],
            data['Count_Credit-Builder Loan'],
            data['Count_Personal Loan'],
            data['Count_Home Equity Loan'],
            data['Count_Not Specified'],
            data['Count_Mortgage Loan'],
            data['Count_Student Loan'],
            data['Count_Debt Consolidation Loan'],
            data['Count_Payday Loan']
        ]

        # Perform prediction
        prediction = model.predict([features])
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error message with status code 500 for Internal Server Error


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
