# WIDS Endterm Submission

**Name:** Arya Patil  
**Program:** Winter in Data Science (WIDS)  


This repository contains my endterm submission for the WIDS program. The work is organized week-wise and documents what I have implemented and solved across the entire course.

---

## Week 1: The Toolbox – Python & NumPy Fundamentals

**Objective:** Build strong foundations in Python, NumPy, and probabilistic thinking.

### Work Done
- Implemented vectorized Monte Carlo simulations using NumPy
- Avoided explicit loops for performance and scalability
- Built simulation-friendly code reusable across experiments

### Key Learnings
- Vectorization vs. looping
- Variance in stochastic processes
- Writing clean, modular simulation code

---

## Week 2: Monte Carlo Estimation & Geometry

**Objective:** Use random sampling to estimate quantities that are difficult to compute analytically.

### Work Done
- Monte Carlo estimation of:
  - π (Pi) using random point sampling
  - Euler’s number (e) using probabilistic stopping-time methods
- Studied convergence behavior by increasing sample size
- Compared Monte Carlo methods with deterministic approaches

### Key Learnings
- Monte Carlo integration
- Law of Large Numbers in practice
- Curse of dimensionality and why Monte Carlo scales better

---

## Week 3: Reinforcement Learning Theory

**Objective:** Develop a rigorous theoretical understanding of Reinforcement Learning.

### Work Done
- Solved theoretical problems involving:
  - Discounted returns
  - Bellman Expectation Equations
  - State-value and action-value functions
- Analyzed reward design and reward hacking
- Studied why exact Dynamic Programming becomes infeasible for large state spaces

### Key Learnings
- Markov Decision Processes (MDPs)
- Role of discount factor γ
- Difference between prediction and control in RL

---

## Week 4: Monte Carlo Prediction & Control (Blackjack)

**Objective:** Learn optimal decision-making purely from experience.

### Work Done
- Implemented Blackjack using the Gymnasium environment
- Monte Carlo Prediction:
  - First-Visit Monte Carlo estimation of state-value function V(s)
  - Evaluated a fixed policy (“Stick at 20 or 21”)
- Monte Carlo Control:
  - Learned action-value function Q(s, a)
  - Used ε-greedy exploration
  - Trained over 500,000 episodes
- Visualized:
  - Learning curve (rolling average reward)
  - Optimal policy heatmap (strategy card)

### Observations
- Strong terminal states have high positive value
- Weak states have strongly negative value
- Even optimal play converges to a negative expected reward due to the house advantage in Blackjack

---


## Tools & Technologies Used

- Python  
- NumPy  
- Matplotlib / Seaborn  
- Gymnasium (Blackjack Environment)

---

## Key Takeaways

- Monte Carlo methods enable learning without explicit environment models
- Vectorization is critical for scalable simulations
- Reinforcement Learning combines probability, optimization, and decision-making
- Exploration–exploitation trade-offs are fundamental
- Even simple games like Blackjack reveal deep insights into stochastic control

---

## Final Notes

- The repository prioritizes clarity, correctness, and conceptual understanding
- Code is written to be modular and reusable
- A detailed **PDF report** accompanies this repository, documenting experiments, results, and reflections from the entire WiDS journey

---

### Submission Components
- GitHub Repository (this repository)
- Endterm Report (PDF, shared via Google Drive)

