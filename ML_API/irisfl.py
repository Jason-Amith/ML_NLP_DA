from flask import Flask, request, jsonify
from sklearn.externals import joblib

HTTP_BAD_REQUEST = 400

app = Flask(__name__)

# Load the model
model = joblib.load('iris-rf-v1.0.pkl')
model_labels = ['setosa', 'versicolor', 'virginica']

@app.route('/predict')
def predict():
    # Retrieve query parameters related to this request.
    sepal_length = request.args.get('sepal_length')
    sepal_width = request.args.get('sepal_width')
    petal_length = request.args.get('petal_length')
    petal_width = request.args.get('petal_width')

    # Our model expects a list of records
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    try:
    # Use the model to predict the class
        label_index = model.predict(features)
    except Exception as err:
        message = ('Failed to score the model. Exception: {}'.format(err))
        response = jsonify(status='error', error_message=message)
        response.status_code = HTTP_BAD_REQUEST
        return response
    
    # Retrieve the iris name that is associated with the predicted class
    label = model_labels[label_index[0]]
    # Create and send a response to the API caller
    return jsonify(status='complete', label=label)

if __name__ == '__main__':
    app.run(debug=True)