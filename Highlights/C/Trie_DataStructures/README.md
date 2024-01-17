
# Associative arrays implemented using tries

## Name:
Leonardo Nigro

## ID:
1235075

This `README.md` file describes an implementation of associative arrays using *tries*, and evaluates when these are superior to the use of a *hash table* based implementation.

# External resources used:

Nonehttps://stackoverflow.com/questions/10598252/remove-first-two-characters-from-a-char-array
https://valgrind.org/docs/manual/quick-start.html
https://opensource.com/article/21/8/copy-files-linux-terminal
https://www.digitalocean.com/community/tutorials/trie-data-structure-in-c-plus-plus
https://www.youtube.com/watch?v=zIjfhVPRZCg
https://www.geeksforgeeks.org/trie-delete/ 


# State of the current implementation

The current implementation can create the nodes and link them to create a trie structure, this structure is fully working but inaccessible by the code given to traverse it
If the user were to manually traverse the root->subtries[0]->subbtries[0]-> ect all data is properly stored and linked but when used by the supplied code segmentaition errors prevent use
due to the inability to create the trie the query and delete functions remain unusable but an attempt was made to implement them anyway
There is a known seg fault caused by line 24 in the trie-iterator (at 0x10ABF0: trie_iterate_chain (trie-iterator.c:24)) it attempts to keybuffer[keybufferpos] = curnode->letter the source of this
issue traces back to curnode->letter not being allocated when trying to reference it, I cannot figure out why curnode->letter does not exist

# Hash tables:

## Strengths:

* Efficient for random access operations.
* Constant time complexity for average case lookup.

## Weaknesses:

* Hash collisions may occur, leading to performance degradation.
* Resizing the table can be an expensive operation.

# Tries:

## Strengths:

* Ideal for applications involving prefix searches. Such as an autocomplete function
* No collisions as each key has a unique path in the trie.

## Weaknesses:

* Can consume more memory compared to hash tables.
* May have slower average case lookup times.

# Summary

## Conditions that would make a hash table appropriate:

Choose a hash table when *ALL* of the conditions in the **required** list are true and any of the conditions in the **preferred** list are true.

### Hash table **required** conditions:
* Memory efficiency is a critical factor.
* Constant time complexity for average case lookup is essential.

### Hash table **preferred** conditions:
* High-speed retrieval is more important than memory efficiency.
* Resizing the table occasionally is acceptable.

## Conditions that would make a trie appropriate:

Choose a trie when *ALL* of the conditions in the **required** list are true and any of the conditions in the **preferred** list are true.

### Trie **required** conditions:
* Prefix searches are a common requirement.
* No tolerance for hash collisions is needed.

### Trie **preferred** conditions:
* Memory usage is not a primary concern.
* Fast average case lookup is essential.