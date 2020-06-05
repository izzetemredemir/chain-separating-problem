# Chain Separating Problem Solution With Python 

Chain Separating Problem also known as Gold Chain Puzzle <br>
[Gold Chain Puzzle Video](https://www.youtube.com/watch?v=CZN26bjRY7g&feature=emb_title)<br>
[Powerpoint page 32-34](https://notendur.hi.is/hh/kennsla/tos/slides05_eng.pdf)
## Problem 
>  A traveler has a gold chain of seven links.•  He must stay at an isolated hotel for seven nights.•  The rent each night consists of one link from the chain.•  What is the fewest number of links that must be cut so that the traveler can pay the hotel one link of the chain each morning without paying for lodging in advance
>
## The Code
In the code I created a lis(`traveller_chains`) which represents firts chain and fill it with numpy zeros. Zeros are represent links of the chain.<br>
`sep_num` is number of how many times the chain cutted. <br>

 ## Solution
  `def split_chain(chain):` <br>

    
### TODO
Code doesn't work for 149 
I should take all possible combination of hotel chains and traveler chains. After that I can find the new payment lists.  Actually I tried it in test.py with ittertools but It didn't work with efficially.<br> 

![screenshot](https://raw.githubusercontent.com/izzetemredemir/chain-separating-problem/master/chain-problem.png)
