#include <stdio.h>
#include <string.h> // for strcmp()
#include <ctype.h> // for isprint()
#include <stdlib.h> // for malloc()
#include <assert.h>

#include "trie_defs.h"


/** recursively roll up the chain */
static int
walk_chain_to_delete(
		void **value,
		TrieNode *curSearchNode,
		AAKeyType key, size_t keylength,
		int *cost
	)
{	
	for(int k = 0; k < curSearchNode->nSubtries; k ++){
		while (curSearchNode->letter == key[k]) {
			if(curSearchNode->nSubtries == 0){
				// i think this works but its hard to test since the insert didnt work
				free(curSearchNode);
			}
			curSearchNode = curSearchNode->subtries[k];
			break;
		}
	}
	// TO DO: remove nodes for deleted key
	return 0;
}

/** delete a key from the trie */
void *trieDeleteKey(
		KeyValueTrie *root,
		AAKeyType key, size_t keylength,
		int *cost
	)
{
	void *valueFromDeletedKey = NULL;


	if (root->nSubtries == 0) {
		return NULL;
	}

	/**
	 ** TO DO: search for the right subchain and delete the key from it
	 **/

	// search through subtries for the primaru key
	
	// first we query to see that the key exists 
	// then we delete all nodes that have nSubtries == 0
	// but we dont have a way to walk backwards in the tries
	// because each parent points to a child but not vise versa
	// so we recurisvely query to the end and delete the last element
	// theres probably a better way online to do this but I find that by actually building all these structures myself I learn way more
	// doesnt help my marks tho.....

	// here is our query iterator
	for(int i = 0; i < root->nSubtries; i ++){
		if(key[0] == root->subtries[i]->letter){
			
			TrieNode* node = root->subtries[i];

			walk_chain_to_delete(NULL, node, key, keylength, cost);

		}
	}


	return valueFromDeletedKey;
}

