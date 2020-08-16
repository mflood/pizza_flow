pizza_flow
==========

Solving bipartite pizza issues using maximum flow

You've ordered some pizzas and you want to make sure everyone
gets to eat pizza slices that they enjoy.

Or, you're considering ordering and you want to get a feel for how many of each pizza you should order.

## Getting started

### How hungry is everyone?

> Add the number of slices of pizza each person anticipates eating

```
b.add_left_node("Flood", 4)
b.add_left_node("Craig", 3)
b.add_left_node("Tavis", 4)
```

### What kind of pizzas are there?

> Define the pizzas and the numbere of slices each contains
> If the same pizza is ordered twice, just double the slices

```
b.add_right_node("Sausage", 8)
b.add_right_node("Pepperoni", 16)
b.add_right_node("Vegetarian", 8)
b.add_right_node("Meat Lovers", 8)
b.add_right_node("Mushroom", 8)
b.add_right_node("Cheese", 8)
```

### Set people's preferences

> For each person, configure the number of slices they would
be willing to eat if they had to.  

```

b.link("Flood", "Meat Lovers", 4)
b.link("Flood", "Vegetarian", 2)

b.link("Tavis", "Vegetarian", 3)
b.link("Tavis", "Mushroom", 3)
b.link("Tavis", "Cheese", 1)

b.link("Craig", "Vegetarian", 3)


```

### Solve it

python pizza_flow.py

