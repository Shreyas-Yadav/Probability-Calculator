# Probability Calculator

A Python project that calculates probability by simulating ball drawings from a hat. It uses a Hat class to manage balls of different colors and provides an experiment function to determine the likelihood of drawing specific combinations. Ideal for understanding probability concepts through practical simulation.

## Classes

### Hat

Represents a hat containing balls of different colors.

#### Methods

- `draw(self, number_of_balls=0)`: Draws a specified number of balls from the hat randomly.

## Functions

### experiment(hat, expected_balls, num_balls_drawn, num_experiments)

Conducts a probability experiment to determine the likelihood of drawing a specific combination of balls from the hat.

#### Parameters

- `hat (Hat)`: The hat object containing the balls.
- `expected_balls (dict)`: A dictionary representing the expected number of each color of balls to be drawn.
- `num_balls_drawn (int)`: The number of balls to draw in each experiment.
- `num_experiments (int)`: The number of experiments to conduct.

#### Returns

- `float`: The probability of drawing the expected combination of balls.

## Usage Example

```python
hat = Hat(blue=3, red=2, green=6)
expected_balls = {'blue': 2, 'green': 1}
num_balls_drawn = 4
num_experiments = 1000
probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(probability)
```
