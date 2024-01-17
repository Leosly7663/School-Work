#include <stdio.h>
#include <string.h> // for strcmp()
#include <ctype.h> // for isprint()
#include <stdlib.h> // for malloc()
#include <assert.h>

#include "trie_defs.h"


/** find a key within the trie */
void *trieLookupKey(
		KeyValueTrie *root,
		AAKeyType key, size_t keylength,
		int *cost
	)
{
	// TO DO: walk the trie to find the key, returning
	// a value if there is one after we have finished
	// our walk
	for(int i = 0; i < root->nSubtries; i ++){
		if(key[0] == root->subtries[i]->letter){
			
			TrieNode* node = root->subtries[i];

			for(int k = 0; k < node->nSubtries; k ++){
				while (node->letter == key[k]) {
					if(node->isKeySoHasValue != 1){
						
					}
					node = node->subtries[k];
					break;
				}
			}
			

		}
	}

	/** return null if the node doesn't have a value */
	return NULL;
}

