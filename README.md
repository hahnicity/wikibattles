# wikibattles
All battles in history (as noted in wikipedia) ranked by significance using page rank algorithm

## Basic
The goal here is to use a well tested and known ranking algorithm, [page rank][2], and apply it 
to all battles in wikipedia. The goal being to rank these battles in order of their significance 
across the english language wikipedia. The hope here is that while history is subjective, we get 
closer to a point of being objective about our results given the assumption that the hive mind that
is wikipedia will yield more impartial results than just one single source.

## Algorithm
The idea here was that I use the [top ranked][1] github project for page rank written in python.
In order to generate the rankings I used data from wikipedia to construct a csv file of
page titles to the battles they were linked to making the ensuing data look like

    <Link from page title>,0,<Link to page title>,1

Where the 0 and 1 denote a weighting on the links s.t. the first page links to the second.
After running the `page_rank.py` module on the data we wrote our output in results.txt.

A problem with this implementation is that it's extraordinarily slow. It took me over an hour 
to run the ranking on an NxN matrix with N = 10^6.

## Results
The results of this run were promising ... # TODO 


[1]: https://github.com/timothyasp/PageRank
[2]: https://en.wikipedia.org/wiki/PageRank
