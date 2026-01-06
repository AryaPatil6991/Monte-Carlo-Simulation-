# WIDS Midterm Submission

**Name:** Arya Patil  
**Program:** Winter in Data Science (WIDS)  


This repository contains my midterm submission for the WIDS program. The work is organized week-wise and documents what I have implemented and solved across the first three weeks of the course.

---

## Week 1: The Toolbox – Python, NumPy & Simulation Basics

### 1. Gambler’s Ruin (`gamblers_ruin`)

In this assignment, I implemented a fully vectorized Monte Carlo simulation of the
classic Gambler’s Ruin problem.

**What I did:**
- Simulated **10,000 gamblers** playing a fair coin-flip game over multiple rounds
- Each gambler starts with the same initial bankroll
- Used **NumPy vectorization only** (no explicit for-loops) to:
  - Generate win/loss outcomes
  - Compute cumulative wealth paths using cumulative sums
- Implemented **bankruptcy handling**, where:
  - Once a gambler’s wealth reaches zero, it remains zero for all future steps
  - Achieved using boolean masking instead of loops
- Created visualizations:
  - Wealth trajectories for a subset of gamblers
  - Mean wealth path across all gamblers
  - Histogram of final wealth distribution

**Key concepts learned:**
- Vectorization vs looping
- Variance in random processes
- Why outcomes spread out even in a fair game (intuition behind CLT)

---

### 2. Game Guide (`game_guide`)

This assignment focused on writing clean, modular Python code using Object-Oriented Programming.

**What I did:**
- Designed a terminal-based game using a **modular OOP structure**
- Separated:
  - Data representation (cards, dice, players, etc.)
  - Game logic and control flow
- Used classes and methods to keep the code reusable and extendable
- Ensured the design is suitable for future **Monte Carlo simulations**, where the
game can be run repeatedly without modification

**Key concepts learned:**
- Object-Oriented Design
- Separation of concerns
- Writing simulation-friendly code

---

## Week 2: Monte Carlo Estimation & Geometry

### Random / Monte Carlo Geometry (`random`)

In this week, I used Monte Carlo methods to estimate mathematical constants and areas.

**What I did:**
- Implemented Monte Carlo estimation of:
  - **π (Pi)** using random point sampling inside a square
  - **Euler’s number (e)** using probabilistic stopping-time methods
- Performed **convergence analysis** by:
  - Running simulations for increasing sample sizes
  - Plotting estimation error against number of samples
- Wrote vectorized code using NumPy for efficiency
- Refactored the simulation into **modular functions**, allowing:
  - Different shapes or functions to be passed as predicates
  - Easy reuse for new Monte Carlo experiments

**Key concepts learned:**
- Monte Carlo integration
- Trade-off between accuracy and number of samples
- Importance of modular design in scientific code

---

## Week 3: Reinforcement Learning Theory

### RL Theory Solutions (`wids_week_3`)

This folder contains **my complete written solutions** to the Week 3 RL theory assignment.

**What I did:**
- Calculated discounted returns for given state trajectories
- Wrote and explained **Bellman Expectation Equations** for specific states and policies
- Analyzed reward design and explained how **reward hacking** occurs
- Explained:
  - Why a discount factor γ < 1 is mathematically necessary
  - How γ affects agent behavior (short-term vs long-term)
- Studied the effect of reward shaping and showed how it can change the optimal policy
- Formulated RL value functions using **linear algebra**
- Estimated computational complexity for large state spaces
- Explained why exact dynamic programming is infeasible and why Monte Carlo methods are needed
- Compared state-value and action-value functions in **model-free RL**

---



## Tools Used
- Python
- NumPy
- Matplotlib

---

## Final Notes
- The focus throughout the submission is on **clarity, correctness, and conceptual understanding**
- All simulations are written in a way that supports scalability and reuse
- Theory assignments are solved step-by-step to strengthen fundamentals before moving to coding-based RL

---
