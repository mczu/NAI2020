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
