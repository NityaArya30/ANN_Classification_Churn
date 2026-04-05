import tensorflow as tf
import pickle

# Load your trained model
model = tf.keras.models.load_model("model.h5")

# Save as .pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model converted to model.pkl")
