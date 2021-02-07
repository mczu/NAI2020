# 1. Testing environment with OpenAI Gym
import gym

env = gym.make('LunarLander-v2')
states = env.observation_space.shape[0]

for i_episode in range(5):
    observation = env.reset()
    score = 0
    for t in range(100):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
    print('Episode:{} Score:{}'.format(i_episode, score))

nb_actions = env.action_space.n  # number of actions in Lunar Lander

# 2.  Creating Model with Keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


model = build_model(states, nb_actions)
model.summary()

# 3. Building Agent with Keras-RL

from rl.agents import DQNAgent, SARSAAgent
from rl.policy import BoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory

# policy = EpsGreedyQPolicy()
policy = BoltzmannQPolicy()
memory = SequentialMemory(limit=10000, window_length=1)
agent = SARSAAgent(model=model, nb_actions=nb_actions, nb_steps_warmup=10, policy=policy)
agent.compile(Adam(lr=1e-4), metrics=['mae'])

# 4. Teaching the agent
steps = 5000

agent.fit(env, nb_steps=steps, visualize=False)

# 5. Testing

agent.test(env, nb_episodes=10, visualize=True)
