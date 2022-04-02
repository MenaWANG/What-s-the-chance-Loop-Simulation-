# A very Interesting Math Question Shown in Python
Let's say I have 3 numbers, two are fake and one is true. I want to find the true one. 

First, out of the three numbers, I will take away a random number. Now you can imagine, among the two left, one must still be fake. Now the judge will take the fake one away. 
  
Here come the million-dollar question: What shall I do? Shall I keep the one I took away first or the one the judge left there? Which choice offers a higher chance of success, or are they equally likely?

# Explanation
Okay, this isn't much of an explanation, the demonstration below explains it way better than me. But let's go over the basic, if we kept the one I took away first, the chances of it being true is 1/3, because I have 3 cards and 2 are fake, let's go over the second example in the demonstration.

Now for the demonstration!

# Demonstration

Number 1 = True

Number 2 = Fake

Number 3 = Fake

So step one, guess a number.

Let's guess number two, so I'll take it away.

Number 1 = True  
Number 3 = Fake

Now the Judge takes away Number 3, because it's fake, and number 1 is true, so I win!

You might think that the chances of anyone guessing the right one is 50%, because the judge takes out only one fake number, and you are only left with a real number and a fake one, but it turns out, the chances of guessing the right one is actually 66.7%.

Why? Because the card you choose at the start is accturally the most important. If you choose a fake one at the start to take out, you are guarranteed to win, try it yourself! (Or with the Python code attached)
