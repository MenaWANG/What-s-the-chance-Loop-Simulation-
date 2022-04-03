# What's the Change? An Interesting Question in Probability
Let's say I have 3 numbers, one of them leads to a big price (let's call it the **TRUE number**) and you can imagine I would like to find it. 

First, out of the three numbers, I will pick a random number. Then among the two left, at least one must still be fake. Now the judge will take the fake one away. 
  
Here come the million-dollar question: What shall I do? Shall I keep the random number I picked first or the one the judge left there? **Which choice offers a higher chance of success, or are they equally likely?**

# Explanation
If we kept the one I picked first, the chances of this number being TRUE is 1/3, because among the three, one is TRUE. 

But how about the chance of success if I switch to the one left by the judge? Is 1/3 too? The answer is NO. Let's look at the simulation below. 

# Simulation

Number 1 = True

Number 2 = Fake

Number 3 = Fake

So step one, guess a number.

Let's guess number two, so I'll take it away.

Number 1 = True  
Number 3 = Fake

Now the Judge takes away Number 3, because it's fake, and number 1 is true, so I win!

You might think that the chances of anyone guessing the right one is 50%, because the judge takes out only one fake number, and you are only left with a true number and a fake one, but it turns out, the chances of guessing the right one is actually 66.7%.

Why? Because the card you choose at the start is actually the most important. If you choose a fake one at the start to take out, you are guarranteed to win, try it yourself! (Or with the Python code attached)
