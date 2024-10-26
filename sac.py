import torch
import torch.nn.functional as F

from agents import GenericACAgent


class SACAgent(GenericACAgent):
    """SAC algorithm."""
    def update_critic(self, obs, action, reward, next_obs, not_done):
        # TODO Start:
        # Hint step 1: Sample the next_action and log_prob of the next action using the self.actor and the next_obs. Use the code 
        # below in update_actor as a refrence on how to do this
        
        # Hint step 2: Sample the two target Q values from the critic_target using next_obs and the sampled next_action. 
        # Take these numbers, and get the target value by taking the min of the 2 q values and then subtracting self.alpha*log_prob
        # The target Q is the reward + (not_done * discount * target_value)
        
        # Hint step 3:
        # Sample the current Q1 and Q2 values of the current state using the critic. The loss is mse(Q1, targetQ) + mse(Q2 + target Q)

        
        # TODO End
        # Optimize the critic
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        return critic_loss.item()

    def update_actor(self, obs):
        # TODO Start:
        
        dist = self.actor(obs)
        action = dist.rsample()
        log_prob = dist.log_prob(action).sum(-1, keepdim=True)
        # TODO: Start
        # Sample the Q1 and Q2 values from the critic and take the minimum value of it. Then calculate the actor loss which
        # is defined by self.alpha * log_prob - actor_Q. Make sure that gradient does not flow through the alpha paramater. 


        # TODO: End

        # optimize the actor
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        # Update the temperature parameter toachieve entropy close to the target entropy
        self.log_alpha_optimizer.zero_grad()
        # TODO Start
        # Calculate the loss for the self.alpha parameter. The loss is defined by self.alpha * (-log_prob
        # - self.target_entropy) Make sure to not pass gradients through the log probs

        # TODO End
        alpha_loss = alpha_loss.mean()
        alpha_loss.backward()
        self.log_alpha_optimizer.step()
        return actor_loss.item(), -log_prob.mean().item(), alpha_loss.item()
