import gym
import evogym.envs
import time
from evogym import sample_robot


if __name__ == '__main__':

    body, connections = sample_robot((5,5))
    env = gym.make('Walker-v0', body=body)
    env.reset()
    start = time.time()

    while True:
        action = env.action_space.sample()-1
        ob, reward, done, info = env.step(action)
        now = time.time()

        if done or now - start > 10:
            break

    env.close()
