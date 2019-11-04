#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
import sys


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length <= 1:
        return None

    # loop through weights and insert index as values into hashtable
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    # loop again to determine if the current weight of index - limit is a current key in ht
    for i in range(len(weights)):
        difference = limit - weights[i]
        # if index is found in ht
        if hash_table_retrieve(ht, difference) is not None:
            # get the index stored as value from inital loop
            index = hash_table_retrieve(ht, difference)
            return(index, i)

    # for i in range(len(weights)):
    #     difference = hash_table_retrieve(ht, weights[i])
    #     if difference is None:
    #         hash_table_insert(ht, limit-weights[i], weights[i])
    #     else:
    #         return (weights[i], difference)

    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
