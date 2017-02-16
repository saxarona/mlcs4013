# 03 notes.md

## ex1

`computeCost` works like this:

1. for each x value of the data, calculate `h = theta(1) + theta(2) * X(i,2)`.
2. Find the square of the difference `h -y(i)` and sum it all.
3. Divide everything over 2m. *Note: This is another version of the mean squared error formula*.

The `gradientDescent` function uses the `computeCost` function to evaluate its cost (the return value of `computeCost`).
After evaluating, a nearby `theta` value is used to calculate the cost, and it is then reduced slowly over `num_iters` times, which is 1500 by default.

The `theta` vector is what we call the `w` weight vector, as seen in class.

Two versions of `computeCost` and `gradientDescent`  were created. These two new versions use the `lambda` value provided in `ex1` at **line 62**, and a variable called `regular`, which is the quadratic regularizer (Eq. 3.29 in Bishop's book).
The cost calculated by these two new functions rise sharply, but the `theta` values found are the same as those found without the regularizer.

A selection of `lambda` values were used: {0, 1, 0.5, 0.05, 0.01} and the result was the same. It seems that 1500 iterations is enough to find the optimal `theta` values for this linear model.

Check the code for the modified `ex1.m` [here](https://gitlab.com/snippets/1602713).
Check the code for the modified `computeCost.m` [here](https://gitlab.com/snippets/1602721).
Check the code for the modified `gradientDescent.m` [here](https://gitlab.com/snippets/1602731).

## tidy-data

In the case of `tidy-data`, the `dist` variable was modified to include the quadratic regularizer. Again, even with a `lambda` value of 1, there's no change in the linear model obtained using regression.

I added a line to the `case-study.r` file provided in the `tidy-data` Github repo around **line 71**, which is this one:

````R
dist = devi['dist'] + norm(hod3["prop_all"], type=c("2"))^2 /2
````