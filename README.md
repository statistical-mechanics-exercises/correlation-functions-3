# The covariance for pairs of spins separated by r sites

In this next exercise, we are going to calculate the covariance between pairs of spins.  I would like you to write a function called covariance spin that takes 2 arguments:

1. `spins` - a list of spin variables that gives the coordinates for a particular microstate.
2. `r` - the distance between the spins that you would like to calculate the correlation between.

Your function should then return the covariance between two spins separated by `r` sites, which is given by:

![](https://render.githubusercontent.com/render/math?math=\langle(s_i\langle\s\rangle)(s_{i%2Br}-\langle\s\rangle)\rangle=\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)(s_{i%2Br}-\langle\s\rangle))

Once again the summation here runs over the ![](https://render.githubusercontent.com/render/math?math=N) spin in the system and the ![](https://render.githubusercontent.com/render/math?math=s_i) values are the spin variables.  Notice, however, that, unlike in the previous exercise, when we expand out the brackets on the right-hand side we do not get the product of the ith spin variable with itself.  We instead have a product of two different spin variables; namely, the ith and (i+r)th spins.  If ![](https://render.githubusercontent.com/render/math?math=\langle\s\rangle=0) the right-hand side of this expression is thus equal to ![](https://render.githubusercontent.com/render/math?math=1/N) times the sum of the product of every pair of spins in the system that are separated by r sites.

Hint: In completing this exercise remember that the spins are on a ring and that ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1), ![](https://render.githubusercontent.com/render/math?math=s_{N%2B2}=s_2) and so on.  You can use the modulo arithmetic that you learnt about when learning to enumerate all the various spin states to ensure that the products of the correct spins are taken i.e. that if r=2 and i=N-1 you calculate the product of ![](https://render.githubusercontent.com/render/math?math=s_{N-1}) and ![](https://render.githubusercontent.com/render/math?math=s_1). 
