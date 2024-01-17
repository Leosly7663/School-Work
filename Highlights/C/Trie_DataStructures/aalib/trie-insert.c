#include <stdio.h>
#include <string.h> // for strcmp()
#include <ctype.h> // for isprint()
#include <stdlib.h> // for malloc()
#include <assert.h>

#include "trie_defs.h"



/** compare a key with the letter in a node */
int
trie_subtreeSearchComparator(const void *keyValue, const void *nodePtr)
{
	TrieNode **node = (TrieNode **) nodePtr;

	AAKeyType key = (AAKeyType) keyValue;
	return (key[0] - (*node)->letter);
}


/** create a whole chain for the rest of the key */
static TrieNode *
trie_create_chain(AAKeyType key, size_t keylength, void *value, int *cost)
{
	TrieNode *current = NULL;
	TrieNode *head = NULL;
	
	
	head = (TrieNode *)malloc(sizeof(TrieNode));
    current = head;

	

	// no known subtries yet
	
	// here we initilize the letter to the first letter of the key
	current->letter=(TrieLetter)key[0];
	current->nSubtries = 0;
	// handle the case of key = 'a' or key = some other 1 letter key
	if(keylength == 1){
		current->isKeySoHasValue=1;
	}else{
		current->isKeySoHasValue=0;
	}
	

	//iterate through the key
	for(int i = 0; i < keylength; i++){
		TrieNode *nextNode = (TrieNode *)malloc(sizeof(TrieNode));
		// initialize a NULL node for us to implant with key data and link to last node
		// no known subtries yet
		current->subtries = (TrieNode **)malloc(10 * sizeof(TrieNode));
		current->subtries[current->nSubtries] = nextNode;
		current->nSubtries++;
		// no known subtries yet 
		nextNode->subtries=NULL;
		// here we initilize the letter to the first letter of the key
		nextNode->letter=(TrieLetter)key[i];
		nextNode->nSubtries=0;
		// handle the case of terminating string
		if(keylength - 1 == i){
			nextNode->isKeySoHasValue = 1;
		}else{
			nextNode->isKeySoHasValue=0;
		}
		
		//printf("Letter: %c, isKeySoHasValue: %d\n", nextNode->letter, nextNode->isKeySoHasValue);
		cost++;

		current = nextNode;
	}
	
	
	// TO DO: create a new chain the the required key letters
	// iterate through the key and create the structure for a the subtrie ( root-000-b-a-n-a-n-a )

	// we are returning the Trie node we create, for reference here is the trie node structure 
	/*
	typedef struct TrieNode {
	 ** if the node we are adding is 'b' it may has other subtries such as 'u' which would link into -u-t-t-e-r
	struct TrieNode **subtries;
	 ** here is where we store the actual letter that is on this level
	TrieLetter letter;
	 ** keep track of how many subtries bc len is hard to get in c :(
	int nSubtries;
	 ** a marker to repersent if this is also a terminal char forming a complete key // there will be one on the last a of banana
	 ** if we were to then add bananas wed iterate down to banana add s to subtries nsubtries++ and in the new 's' node set isKeySoHasValue to 1
	int isKeySoHasValue;
	void *value;
	}
	*/
	

	return head;
}

/** add the given chain to the list of tries in the current node */
// add chain links the newly created chain to the root array that holds each primary letter node
static int
trie_add_chain(
		TrieNode **subtreeList, int nSubtries,
		AAKeyType key,
		TrieNode *newChain
	)
{
	// TO DO:  add the provided chain to the node; the first letter
	// of the key may be used to organize where within the set of
	// subtries you add this

	// okay so for this one we know that the primary key does not exist in the root level
	// this is more simple to build out
	// we use the first function to create the key into a linked node set and then we just have to go in and set root->subtries[ VALUE ] = current and then make the node off it
	// like this root->subtries[root->nSubtries++] = trie_create_chain(key, keylength, value, cost);
	// we want to try to organize this alphabetically and I have a fun way to do it!
	// there is optimizing potential here to make finding the primary node easier, if we remember our subtries are 256 NULL types and we save each primary node under root->subtries[n]
	// where n is the ascii of the key[0] then the first call to find our starting node will be O(1) because we'll go straight to it every time without having to iterate through to find
	// where key[0] == root->subtries[i]->letter

	//is it really this easy?

	subtreeList[(int)key[0]-'A'] = newChain;
	

	// TO DO: you probably want to replace this return statement
	// with your own code
	return -1;
}

// ** thinking out loud
/** link the provided key into the current chain */
// in an example "a-r-r-a-y" is already in the nodes, we pass key="are" we find that the primary letter and key a=a and then from there we call this function
// with that in mind we compare key[1] and subtries[i]->letter for i = nSubTries 
// if we find a match that subtrie becomes the current node and then we restart the search looking through the subtries[i]->letter comparing it to key[i]
// if we DONT find a match then we can say that we need to create a new subtrie 
// now heres the thing
// we can say that from a-r- we can say key='e' and quickly chain and link just that saving us from creating the whole a-r-e chain, linking r-e in a-r-r-a-y
// but for this we need to say that key = key[minus the first 2 elements]
// but that would require iterating through the key to remake the key - i letter
// we could aslo instead NOT use the create chain function and instead create a new chain starting from i saving computational speed, this would be less clean but more efficent
// this implementation also allows for me to not have to free a and r from 'a-r-e'

static int
trie_link_to_chain(TrieNode *current,
		AAKeyType key, size_t keylength,
		void *value, int *cost)
{
	// TO DO: add the remaining portions of the key
	// into this chain, forming a new branch if and when
	// they stop matching existing letters within the subtries

	// first well need to iterate through the node to find our point of divergance
	// this function is only going to be called when key[0] exists in the root subtries so we know key[0] == current->letter
	// from there we check if current->subtries[i]->letter = key[x] i = 1 ++, iterate through all subtrie letters if one is found current= current->subtrie[i] and x++ and restart loop until not found

	for(int x = 0 ; x < keylength ; x++){
		for(int j = 0 ; j < current->nSubtries ; j++){
			if(current->subtries[j]->letter != key[x]){
				
				if(x == keylength && current->isKeySoHasValue == 1){
					// this return basically says HEY that key already exists in the library dumby
					return -1;
				}else{
					// this handles the creation of the remaining chain to be linked to the current node
					//iterate through the key
					for(int i = x; i < keylength; i++){
						// initialize a NULL node for us to implant with key data and link to last node
						TrieNode *nextNode = NULL;
						nextNode = (TrieNode *)malloc(sizeof(TrieNode));
						// initialize a NULL node for us to implant with key data and link to last node

						nextNode->subtries = (TrieNode **)malloc(10 * sizeof(TrieNode));
						// no known subtries yet
						current->subtries[i] = nextNode;
						current->nSubtries++;
						// no known subtries yet 
						// here we initilize the letter to the first letter of the key
						nextNode->letter=key[i];
						nextNode->nSubtries=0;
						// handle the case of terminating string
						if(keylength - 1 == i){
							nextNode->isKeySoHasValue = 1;
						}else{
							nextNode->isKeySoHasValue=0;
						}
						
						//printf("Letter: %c, isKeySoHasValue: %d\n", nextNode->letter, nextNode->isKeySoHasValue);
						cost++;

						current = nextNode;
						nextNode = NULL;
						nextNode = (TrieNode *)malloc(sizeof(TrieNode));
					}
				}
				
			}
			else if(current->subtries[j]->letter == key[x]){
				current = current->subtries[j];
				break;
			}
		}
	}
	

	// TO DO: you probably want to replace this return statement
	// with your own code
	return 1;
}

//nt h= 0;
//int l= -1;

int
trieInsertKey(KeyValueTrie *root,
		AAKeyType key, size_t keylength,
		void *value, int *cost)
{	
	
	/** keep the max key length in order to keep a buffer for interation */
	if (root->maxKeyLength < keylength)
		root->maxKeyLength = keylength;
	

	// if there are no subtries then create the first one at root ascii [key[0]]
	if (root->nSubtries == 0) {
		root->subtries[(int)key[0]-'A'] = trie_create_chain(
				key, keylength, value, cost);
				root->nSubtries++;
		return 0;
	}

	if(root->subtries[(int)key[0]-'A'] != NULL){
		//printf("LINKING\n");
		if(key[0] == root->subtries[(int)key[0]-'A']->letter){
			trie_link_to_chain(root->subtries[(int)key[0]-'A'], key, keylength, value, cost);
			//l++;
		}
	
	}
	else{
		//printf("CHAINING\n");
		trie_add_chain(root->subtries, root->nSubtries++, key, trie_create_chain(key, keylength, value, cost));
		//h++;
		//l = 0;
	}
	
	//printf("|%d| ",root->nSubtries);
	//printf("|%d| ",h);
	//printf("{%c}",root->subtries[0]->letter);

	//printf("%c",root->subtries[h]->subtries[0]->letter);
	//printf("%c",root->subtries[h]->subtries[0]->subtries[0]->letter);
	// TO DO: find the subtrie with the leading letter of the
	// key, and insert the new key into the correct subtrie
	// chain based on that letter

	// TO DO: you probably want to replace this return statement
	// with your own code
	return 1;
	
}


