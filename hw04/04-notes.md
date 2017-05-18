# 04 SVM Notes

Hey.
I'm doing an SVM on Octave using the `libsvm` [package](https://www.csie.ntu.edu.tw/~cjlin/libsvm/).
This file contains some useful info about the homework assignment like bibliography entries and general concepts of the SVM notation.
Besides, I like doing these markdown-styled notebooks.

## QuickNav

1. [What we got so far](#what-we-got-so-far)
2. [What's next](#what's-next)
3. [The dataset](#the-dataset)

## What we got so far

I, somehow, managed to *somewhat* understand what an SVM is and how does it work. I used two incredibly good resources:

1. A complete explanation of SVMs as quadratic optimization problems and such by Andrew Ng (of course). It is explained [here](http://cs229.stanford.edu/notes/cs229-notes3.pdf). A decent understanding of optimization (what's a primal, its dual and such) is recommended.
2. An ELI5 (Explain Like I'm 5-years-old) explanation which is [here](https://www.reddit.com/r/MachineLearning/comments/15zrpp/please_explain_support_vector_machines_svm_like_i/). The analogy of the villain and the ninja powers is incredibly enlightening.

I now joined all available data in different training files using a Python script which can be found [here](04-preprocessing.py). I just need to make the SVM work and start writing about it!

## What's next

My next move is to train the SVM (which is pretty easy to use following the examples of Stanford Open Classroom's activity) with the data provided. The Open Classroom activity is located [here](http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex7/ex7.html).

Maybe plot data and test accuracy and such.
Sounds easy enough, so I'll do it tomorrow or so.

## The dataset

Thing is, our data was horribly presented in separated files, so I joined them all in a single file and modified its presentation so that it could be read by `libsvmread`. The dataset is located [here](https://archive.ics.uci.edu/ml/datasets/Artificial+Characters).

This dataset represent artificially created characters which can be of **10 different classes**, ranging from 1 to 10, namely: A, C, D, E, F, G, H, L, P and R.

This is the data format:

> CLASS OBJNUM TYPE XX1 YY1 XX2 YY2 SIZE DIAG

`CLASS` is our *y*, of course.
We can ignore `OBJNUM`, since it's just the number of the instance.
However, `TYPE`, `XX` and `YY` coordinates, and both `SIZE` and `DIAG` are useful attributes that we wish to keep in our dataset.

Originally, the data was stored in the format presented above, but `libsvmread` can only read data in sparse format, like this:

> 1 2:1 3:3 4:2 5:1 6:20

In this format, each data attribute is separated by a space. The number on the left of the colon represents the number of the attribute: first, second, *n*-column. The value of each attribute is described using the number on the right of the colon. Therefore, `8:20` means that the eighth attribute has a value of 20, which means that the `SIZE` attribute of this data point is 20.
It is important to note that the first attribute is always 1 or -1, which is the class of each example. Thing is, `libsvm` only works on two-class datasets (that is, if it belongs to a class, or not). Since we're dealing with 10 classes, we need to train 10 SVMs. Oh god.

Nevertheless, it's already done. Now on to training!