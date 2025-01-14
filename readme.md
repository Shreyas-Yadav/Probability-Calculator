# Probability Calculator

This project implements a probability calculator that simulates drawing balls from a hat to calculate probabilistic outcomes.

## Description

The program contains two main classes/functions:

### `Hat` Class
A class that represents a hat containing colored balls:
- Initialize with a variable number of balls of different colors
- Supports drawing a random selection of balls
- Automatically refills drawn balls after experiments

### `experiment` Function
Calculates probability by running multiple experiments:
- Takes parameters for expected ball counts and experiment configuration
- Returns probability of drawing the expected combination of balls
- Runs specified number of experiments to calculate probability

## Usage Example

```python
# Create a hat with colored balls
hat = Hat(blue=3, red=2, green=6)

# Define expected outcome
expected_balls = {'blue': 2, 'green': 1}

# Configure experiment
num_balls_drawn = 4
num_experiments = 1000

# Run the experiment
probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)