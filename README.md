# wikibattles
![intro](http://horroretc.com/wp-content/uploads/2011/05/189.jpg)

All battles in history (as noted in wikipedia) ranked by significance using page rank algorithm

## Basic
The goal here is to use a mature and well known ranking algorithm, [page rank][2], better known 
as the Google algorithm, and apply it to all battles in wikipedia. We want to rank these battles 
in order of their importance across the english language wikipedia. The hope here is that while 
history is subjective, we get closer to a point of being objective about our results given the 
assumption that the hive mind that is wikipedia will yield more impartial results than just one single source.

## Data
All data from this project was gathered from the [07/02/2015][4] data dump of wikipedia. The database used for
this project was MariaDB but any MySQL derivative can be used. The goal was to find all wikipedia pages that
linked to a specific battle. After finding all historical battles and all pages that linked to them we could
then implement the algorithm and rank the battles in terms of importance.

## Algorithm
The idea here was that I use the [top ranked][1] github project for page rank written in python.
After rewriting the code to fix bugs and make it a bit faster I looked into how the data for the
algorithm must be laid out. The data I used was meant to construct a csv file of page titles to the 
battles they were linked to making the ensuing data look like

    <Link from page title>,0,<Link to page title>,1

Where the 0 and 1 denote a weighting on the links s.t. the first page links to the second.
After running the `page_rank.py` module on the data in `battlelinks.csv` we wrote our output to `results.txt`.

## Results
The top 50 battles as noted by the page rank algorithm were:

     1 Battle_of_France               
     2 Battle_of_Britain              
     3 Battle_of_the_Atlantic         
     4 Battle_of_the_Bulge            
     5 Battle_of_Stalingrad           
     6 Battle_of_Alberta              
     7 Battle_of_Midway               
     8 Battle_of_the_Coral_Sea        
     9 Battle_of_Ontario              
    10 Battle_of_Gettysburg           
    11 Battle_of_Quebec_(ice_hockey)  
    12 Battle_of_Okinawa              
    13 Battle_of_Moscow               
    14 Battle_of_Berlin               
    15 Battle_of_Hong_Kong            
    16 Battle_of_Kursk                
    17 Battle_of_Plassey              
    18 Battle_of_Caporetto            
    19 Battle_of_Belgium              
    20 Battle_of_the_Netherlands      
    21 Battle_of_Crete                
    22 Battle_of_Waterloo             
    23 Battle_of_Deçiq               
    24 Battle_of_Leyte_Gulf           
    25 Battle_of_Iwo_Jima             
    26 Battle_of_Cable_Street         
    27 Battle_of_Kiev_(1941)          
    28 Battle_of_Monte_Cassino        
    29 Battle_of_Narva_(1944)         
    30 Battle_of_Vittorio_Veneto      
    31 Battle_of_Asiago               
    32 Battle_of_the_Somme            
    33 Battle_of_Smolensk_(1943)      
    34 Battle_of_Greece               
    35 Battle_of_Jutland              
    36 Battle_of_Borneo_(1941–42)   
    37 Battle_of_St_Matthew's         
    38 Battle_of_Rzhev,_Summer_1942   
    39 Battle_of_Shumshu              
    40 Battle_of_Manila_(1945)        
    41 Battle_of_Stockton             
    42 Battle_of_Changsha_(1939)      
    43 Battle_of_Changde              
    44 Battle_of_Changsha_(1941)      
    45 Battle_of_Changsha_(1942)      
    46 Battle_of_West_Hunan           
    47 Battle_of_the_Java_Sea         
    48 Battle_of_Trafalgar            
    49 Battle_of_Antietam             
    50 Battle_of_Singapore            

Most of the battles here are from World War 2. Of interest is that this list has a decidedly Western 
Europe/USA focus as exemplified by a battle as major as the [Battle of Shanghai][3] being left off 
this list whereas clashes between anti/pro facist demonstrators in England are represented by the 
Battles of Stockton and Cable Street on the top 50. So it must be taken into consideration that these
results are distorted by the lens of living in an English speaking country.

What didn't fit my hypothesis was that page rank would rank battles by importance across history. Rather, it 
seemed to rank battles by scale and relevance to current times. I think this makes sense given that 
wikipedia is composed of a collection of pages written by individuals since 2001. Given that World War 2 most
directly shaped our modern world it is linked more heavily than earlier conflicts.

The above explanation would support the observation of the Battles of Alberta, Ontario, and Quebec being highly
ranked alongside pages such as the Battle of Okinawa. These are not actually historical battles but hockey
rivalries and so they may have a much larger influence on the lives of people today than something like 
Gettysburg.

[1]: https://github.com/timothyasp/PageRank
[2]: https://en.wikipedia.org/wiki/PageRank
[3]: https://en.wikipedia.org/wiki/Battle_of_Shanghai
[4]: https://dumps.wikimedia.org/enwiki/20150702/
