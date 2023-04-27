# Code for calculating integrals

The downside of a numerical method is that it can only find an approximate answer.

An advantage of numerical methods is that we can easily integrate a function f .x/ that is only known as samples, i.e., discrete values at some x points,
and not as a continuous function of x expressed through a formula. This is highly
relevant when f is measured in a physical experiment.

Trapezoidal General Formula:
$$\int_a^b f(x)\. dx \approx h\left(\frac{1}{2}f(x_0) + \sum_{i=1}^{n-1}f(x_i) + \frac{1}{2}f(x_n)\right)$$

Midpoint General Formula:
$$\int_a^b f(x)\. dx \approx h\left(\sum_{i=1}^{n-1}f(x_i)\right), \text{where } x_i = (a + \frac{h}{2} + i.h)$$


