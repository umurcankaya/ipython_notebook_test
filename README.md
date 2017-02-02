# ipython_notebook_test

Testing the markdown language

## How to add code

```python
import numpy as np
import matplotlib.pyplot as plt
```
```python
t = np.linspace(0,10,1000)
y = np.sin(t)
```
```python
plt.plot(t,y)
plt.show()
```
## How to insert figure
http://solutionoptimist.com/2013/12/28/awesome-github-tricks/
![alt tag](https://cloud.githubusercontent.com/assets/17966893/22561723/192f5dc4-e982-11e6-9ba8-32ad9aa3acc3.png)

## How to do math

**Hamilton's Principle:** Of all the possible trajectories of a system that connect the configurations $q_1$ and $q_2$ in the interval $[t_1,t_2]$, the actual motion $q^*(t)$ makes the action functional $S(q)$ of the system stationary.
$$ S(q) = \int_{t_1}^{t_2} L(q, \dot q, t)dt $$
$$\delta S = 0$$


```
