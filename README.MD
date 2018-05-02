# Code Exercise
Our goal with this coding exercise is to test your ability to write code, 
debug, and craft unit tests. This coding exercise shouldn't take you more than 
a couple of hours to finish.

# Premise
The premise behind this project is that your team has started on it. It was in 
the middle of development when a higher priority project forced them to switch 
off of this work. It has been handed to you and you are expected to finish it.

# To Do
The following methods from graph_stuff.py have bugs in them that you are 
expected to fix:
* construct_graph
* delete_nodes
* find_disconnected_nodes
The following methods from tree_stuff.py are not implemented and should be:
* construct_tree
* hash_tree

There is also missing logic in main.py, in execute, that you are expected to 
add. You should also create any unit tests you think are necessary. Lastly, Leave an explanation of what tools you used in this work and how you solved 
the problem in the README. This gives you an opportunity to tell us anything 
you think is important for documentation purposes.

# Setup
In order to ensure that others don't copy your work explicitly by looking at a 
fork, we ask that you clone this repo, change the remote to your personal 
Github repository, and push the code. For our evaluation purposes, it is 
helpful if you push all of this code in one commit called "init" and then 
commit the changes for your solution as you see fit.

# Code Functionality
The code should perform the following steps:
* Accept a string as a command line argument. It should only accept a string 
with an even number of characters, otherwise throw a runtime error.
* Find the most frequent character in the string. If multiple characters have 
the same count, take the first occurring one as the most frequent.
* Split the string into two equal halves.
* Construct a undirected graph where each node corresponds to a character 
(each character should be represented by at most one node, so subsequent 
repeat characters only create edges, not nodes) in the first half of the 
string and edges are between characters that are next to each other.
* Delete node in the graph corresponding with the most frequent character.
* Find any nodes that are disconnected from the graph, e.g. no edges.
* Construct a binary search tree from characters in the second half of the 
string. Repeated characters will be considered lower than the previous 
instance of that character that was already added.
* MD5 hash the character in each node of the tree from tree leafs all the way 
to the top except nodes that were disconnected from the graph. This should be 
hash up the tree like "*left_hash*-*parent_character*-*right_hash*" where 
*left_hash* is the left child nodes hash, *right_hash* is the right child 
nodes hash, and *parent_character* is the parent nodes character. E.g. 
![d/d\f][tree.png]
would be "8277e0910d750195b448797616e091ad-d-8fa14cdd754f91cc6554c9e71929cce7" 
If left or right is missing, simply omit the dash and hash for that node when 
calculating the parent hash.
If a parent node is supposed to be omitted because it is a disconnected node 
from the graph, simply omit the dash and character for that node when 
calculating its hash.
* Print out hash.

# Notes
None of the code is particularly well written. You are allowed to modify or add 
anything you want as long as you keep and implement the following method stubs:
* construct_graph
* delete_nodes
* find_disconnected_nodes
* construct_tree
* hash_tree
* frequent_character
* split_string

You must not alter the architectural design of the methods in graph_stuff.py 
because this is to show that you can debug code written by others. If you do 
not appreciate how this particular code is written, you are welcome to leave 
comments for us to look at.

Note that minimal testing of the execute function has been provided to allow 
you to check your work.