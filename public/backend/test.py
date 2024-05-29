import pickle

# Step 1: Load the model
model_path = 'svm_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Step 2: Prepare the test data
import numpy as np

test_data = np.array([[5.1, 3.5, 1.4, 0.2],  # Example for a classification model
                      [6.2, 3.4, 5.4, 2.3]])

# Step 3: Make predictions
predictions = model.predict(test_data)

# Step 4: Verify the output
print("Predictions:", predictions)
