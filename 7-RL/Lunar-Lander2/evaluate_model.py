from tensorflow import keras
from keras.models import model_from_json
import gym
import matplotlib.pyplot as plt
import numpy as np

# load json and create model
json_file = open('main_model_json.json', 'r')
main_model_json = json_file.read()
json_file.close()
main_model = model_from_json(main_model_json)
# load weights into new model
main_model.load_weights("main_model_json.h5")
print("Loaded model from disk")

# load json and create model
json_file = open('target_model_json.json', 'r')
target_model_json = json_file.read()
json_file.close()
target_model = model_from_json(target_model_json)
# load weights into new model
target_model.load_weights("target_model_json.h5")
print("Loaded model from disk")


def simulate_agent(env, model):
    state = env.reset()
    done = False
    while not done:
        env.render()
        action = np.argmax(model.predict([state.reshape(1,-1)]))
        state, reward, done, _ = env.step(action)
    env.close()


env = gym.make("LunarLander-v2")
simulate_agent(env, target_model)
